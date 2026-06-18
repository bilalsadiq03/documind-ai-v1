import os
import json
import shutil
import redis
from git import Repo
from repo_analyzer import collect_files
from repo_analyzer import build_prompt

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

QUEUE_NAME = "documind:jobs"
WORKDIR = "./repos"

os.makedirs(WORKDIR, exist_ok=True)

print("Worker started...")

while True:

    _, raw_job = redis_client.brpop(QUEUE_NAME)

    job = json.loads(raw_job)

    job_id = job["job_id"]
    repo_url = job["repo_url"]

    print(f"Processing {job_id}")
    print(f"Repository: {repo_url}")

    repo_path = os.path.join(WORKDIR, job_id)

    try:

        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)

        Repo.clone_from(
            repo_url,
            repo_path,
            depth=1
        )

        print("Clone successful")

        files = collect_files(repo_path)

        print(f"Collected {len(files)} files")

        prompt = build_prompt(files)

        print("Prompt Length:", len(prompt))

    except Exception as e:
        print("Clone failed")
        print(e)