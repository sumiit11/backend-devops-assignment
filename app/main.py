from fastapi import FastAPI
from app.tasks import process_job
from app.database import collection
import uuid

app = FastAPI()

@app.post("/jobs")
async def create_job():
    job_id = str(uuid.uuid4())

    job = {
        "job_id": job_id,
        "status": "pending"
    }

    await collection.insert_one(job)

    process_job.delay(job_id)

    return {"job_id": job_id}

@app.get("/jobs/{job_id}")
async def get_job(job_id: str):
    job = await collection.find_one({"job_id": job_id})

    if job:
        return {
            "job_id": job["job_id"],
            "status": job["status"]
        }
    return {"error": "job not found"}