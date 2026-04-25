from fastapi import APIRouter
import uuid
from app.tasks import process_job
from app.db import jobs_collection

router = APIRouter()

@router.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())

    jobs_collection.insert_one({
        "job_id": job_id,
        "status": "pending"
    })

    process_job.delay(job_id)

    return {"job_id": job_id}

@router.get("/jobs/{job_id}")
def get_job(job_id: str):
    job = jobs_collection.find_one({"job_id": job_id})

    if not job:
        return {"job_id": job_id, "status": "not found"}

    return {
        "job_id": job_id,
        "status": job["status"]
    }