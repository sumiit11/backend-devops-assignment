from celery import Celery
import time
from app.db import jobs_collection

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def process_job(job_id):
    print(f"Processing job {job_id}")

    jobs_collection.update_one(
        {"job_id": job_id},
        {"$set": {"status": "processing"}}
    )

    time.sleep(5)

    jobs_collection.update_one(
        {"job_id": job_id},
        {"$set": {"status": "done"}}
    )