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

3. Architecture Diagram (REQUIRED)

Your README must include a diagram like:

        ┌──────────────┐
        │   Client     │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │  FastAPI     │  (ECS)
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   Redis      │  (ElastiCache)
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ Celery Worker│  (ECS)
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ MongoDB      │



POST /jobs → create job  




GET /jobs/{job\_id} → check status  



\## Flow

pending → processing → done

Project structure

Example:

app/
  api/
  workers/
  models/
docker/
.github/workflows/

. AWS Architecture explanation (THIS IS CRITICAL)
You should explain like this:
Example (what reviewers expect):

We use ECS Fargate to run containerized services without managing servers.
Redis is hosted on ElastiCache to provide low-latency queueing for Celery.
MongoDB stores job states and results.
Docker images are stored in ECR and deployed via GitHub Actions.


4. CI/CD explanation
Explain:


what happens on push


how deployment works



🚨 Common mistakes (check your repo)
If you’ve “added necessary things”, verify these:
❌ Missing deploy step
Many people only:


build image


push image
👉 but NEVER deploy → FAIL



❌ No architecture diagram
👉 automatic rejection risk

❌ No explanation of why services chosen
👉 not just WHAT, but WHY

❌ Hardcoded secrets
👉 must use .env + GitHub secrets

🧪 Quick self-check checklist
Answer YES to all:


 GitHub Actions deploys to AWS automatically


 Uses ECR (or equivalent)


 Uses ECS / EC2 / Beanstalk properly


 README has architecture diagram


 README explains service choices


 README explains deployment flow


 Clean commit history (not 1 commit)






