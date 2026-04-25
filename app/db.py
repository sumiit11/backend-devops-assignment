from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["devops_db"]
jobs_collection = db["jobs"]