from pymongo import MongoClient
from configs import MONGO_URI, DB_NAME


def get_db():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return client, db