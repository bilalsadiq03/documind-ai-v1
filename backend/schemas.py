from pydantic import BaseModel

class JobRequest(BaseModel):
    repo_url: str