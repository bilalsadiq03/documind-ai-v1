from fastapi import FastAPI
from schemas import JobRequest
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

    return{
        "job_id": job_id,
        "status": "queued"
    }
