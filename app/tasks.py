from app.worker import celery_app
from pymongo import MongoClient
import time

# Connect to MongoDB (Docker service name)
client = MongoClient("mongodb://mongo:27017")
db = client["task_db"]
collection = db["jobs"]

@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def process_job(self, job_id):
    print(f"Processing job: {job_id}")

    # Update status → processing
    collection.update_one(
        {"job_id": job_id},
        {"$set": {"status": "processing"}}
    )

    time.sleep(5)

    # Update status → done
    collection.update_one(
        {"job_id": job_id},
        {"$set": {"status": "done"}}
    )

    print(f"Completed job: {job_id}")