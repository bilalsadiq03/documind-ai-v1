from fastapi import FastAPI
from schemas import JobRequest
from jobs import jobs
from queue_service import enqueue_job
import uuid

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Documind API running..."
    }

@app.post("/generate")
def generate(job: JobRequest):
    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "id": job_id,
        "repo_url": job.repo_url,
        "status": "queued"
    }

    enqueue_job({
        "job_id": job_id,
        "repo_url": job.repo_url
    })

    return{
        "job_id": job_id,
        "status": "queued"
    }

@app.get("/jobs/{job_id}")
def get_job(job_id: str):

    if job_id not in jobs:
        return {
            "error": "Job not found"
        }
    
    return jobs[job_id]
