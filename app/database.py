from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection (Docker service name: mongo)
client = AsyncIOMotorClient("mongodb://mongo:27017")

# Database name
db = client["task_db"]

# Collection name
collection = db["jobs"]