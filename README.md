\# Backend DevOps Assignment



\## Tech Stack

\- FastAPI

\- Redis

\- Celery

\- MongoDB

\- Docker



\## How to Run



\### 1. Start Redis

docker run -d -p 6379:6379 redis



\### 2. Start MongoDB

docker run -d -p 27017:27017 mongo



\### 3. Start Celery

cd backend-devops-assignment

venv\\Scripts\\activate

set PYTHONPATH=%CD%

python -m celery -A app.tasks worker --pool=solo --loglevel=info



\### 4. Start FastAPI

python -m uvicorn app.main:app --reload



\## API



POST /jobs → create job  

GET /jobs/{job\_id} → check status  



\## Flow

pending → processing → done

