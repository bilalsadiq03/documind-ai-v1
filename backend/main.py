from fastapi import FastAPI
from schemas import JobRequest
from queue_service import enqueue_job
from models import Job
from database import SessionLocal
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Documind API running..."
    }

@app.post("/generate")
def generate(job: JobRequest):

    job_id = str(uuid.uuid4())

    db = SessionLocal()

    db_job = Job(
        id=job_id,
        repo_url=job.repo_url,
        status="queued"
    )

    db.add(db_job)
    db.commit()

    db.close()

    enqueue_job({
        "job_id": job_id,
        "repo_url": job.repo_url
    })

    return {
        "job_id": job_id,
        "status": "queued"
    }


@app.get("/jobs/{job_id}")
def get_job(job_id: str):

    db = SessionLocal()

    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    db.close()

    if not job:
        return {
            "error": "Job not found"
        }

    return {
        "id": job.id,
        "status": job.status,
        "readme_path": job.readme_path
    }


@app.get("/jobs/{job_id}/readme")
def get_readme(job_id: str):

    db = SessionLocal()

    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    db.close()

    if not job:
        return {
            "error": "Job not found"
        }

    if job.status != "completed":
        return {
            "error": "README not ready"
        }

    with open(job.readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    return {
        "content": content
    }

@app.get("/jobs/{job_id}/download")
def download_readme(job_id: str):

    db = SessionLocal()

    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    db.close()

    if not job:
        return {"error": "Job not found"}

    return FileResponse(
        path=job.readme_path,
        filename="README.md",
        media_type="text/markdown"
    )