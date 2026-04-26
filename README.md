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

 ## AWS Deployment Architecture

We use AWS ECS Fargate to run containerized services without managing servers.

- API and Celery workers run as ECS services
- Docker images are stored in Amazon ECR
- Redis is hosted using ElastiCache
- MongoDB is hosted on MongoDB Atlas
- CloudWatch is used for logs and monitoring


 README explains deployment flow


 Clean commit history (not 1 commit)



Add this (simple + effective)
## Architecture Diagram

Client → FastAPI (ECS)
        ↓
     Redis (ElastiCache)
        ↓
     Celery Worker (ECS)
        ↓
     MongoDB (Atlas)


Production-Grade Task Queue Service

A scalable, containerized job processing system built with FastAPI, Celery, Redis, and MongoDB. This project simulates a real-world backend system with asynchronous task execution, observability, and automated deployment.

📌 Features
Async job processing with Celery
REST API with FastAPI
Redis as message broker
MongoDB for persistence
Rate limiting using Redis
Prometheus metrics + Grafana dashboards
Structured JSON logging
Fully containerized with Docker
CI/CD pipeline using GitHub Actions
AWS-ready deployment architecture
🏗️ Architecture Overview
🔄 System Flow

Client → FastAPI API → Redis Queue → Celery Worker → MongoDB

☁️ AWS Architecture
Client
   ↓
FastAPI (ECS Fargate)
   ↓
Redis (ElastiCache)
   ↓
Celery Worker (ECS Fargate)
   ↓
MongoDB (MongoDB Atlas)
🧠 Design Decisions
FastAPI

Chosen for its high performance, async support, and clean API design.

Celery + Redis

Used for distributed background job processing with retry and fault tolerance.

MongoDB

Flexible schema to store job states and results efficiently.

ECS Fargate

Selected to run containers without managing servers, enabling easy scaling and deployment.

ElastiCache (Redis)

Provides low-latency queueing required for task processing.

Prometheus + Grafana

Used for monitoring metrics and visualizing system performance.

📁 Project Structure
.
├── app/
│   ├── api/          # FastAPI routes
│   ├── workers/      # Celery worker logic
│   ├── models/       # MongoDB models
│   └── core/         # config & utilities
├── docker/
├── docker-compose.yml
├── .github/workflows/
└── README.md
⚙️ Running Locally
1. Clone the repo
git clone https://github.com/sumiit11/backend-devops-assignment.git
cd backend-devops-assignment
2. Setup environment variables
cp .env.example .env
3. Start all services
docker compose up --build 




