import os
import json
import shutil
import redis
from git import Repo

from repo_analyzer import collect_files, build_prompt
from gemini_client import generate_readme
from database import SessionLocal
from models import Job

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

QUEUE_NAME = "documind:jobs"
WORKDIR = "./repos"
OUTPUT_DIR = "../storage/generated"

os.makedirs(WORKDIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Worker started...")

while True:
    try:
        _, raw_job = redis_client.brpop(QUEUE_NAME)

        job = json.loads(raw_job)

        job_id = job["job_id"]
        repo_url = job["repo_url"]

        db = SessionLocal()

        job_record = (
            db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

        if job_record:
            job_record.status = "processing"
            db.commit()

        print("\n" + "=" * 50)
        print(f"Processing Job: {job_id}")
        print(f"Repository: {repo_url}")
        print("=" * 50)

        repo_path = os.path.join(WORKDIR, job_id)

        # =========================
        # Clone Repository
        # =========================
        try:
            if os.path.exists(repo_path):
                shutil.rmtree(repo_path)

            print("Cloning repository...")

            Repo.clone_from(
                repo_url,
                repo_path,
                depth=1
            )

            print("Clone successful")

        except Exception as e:
            print("Clone failed")
            print(e)
            continue

        # =========================
        # Analyze Repository
        # =========================
        try:
            print("Collecting files...")

            files = collect_files(repo_path)

            print(f"Collected {len(files)} files")

            prompt = build_prompt(files)

            print(f"Prompt Length: {len(prompt)}")

        except Exception as e:
            print("Repository analysis failed")
            print(e)
            continue

        # =========================
        # Generate README
        # =========================
        try:
            print("Generating README...")

            readme = generate_readme(prompt)

            print("README generated")
            print(f"README Length: {len(readme)}")

        except Exception as e:
            print("Gemini generation failed")
            print(e)
            continue

        # =========================
        # Save README
        # =========================
        try:
            output_file = os.path.join(
                OUTPUT_DIR,
                f"{job_id}.md"
            )

            with open(
                output_file,
                "w",
                encoding="utf-8"
            ) as f:
                f.write(readme)

            print(f"README saved: {output_file}")

            if job_record:
                job_record.status = "completed"
                job_record.readme_path = output_file
                db.commit()

        except Exception as e:
            print("Failed to save README")
            print(e)
            continue

        print(f"Job {job_id} completed successfully")

    except Exception as e:

        if job_record:
            job_record.status = "failed"
            db.commit()

        print(e)