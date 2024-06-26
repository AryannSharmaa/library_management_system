from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("uri")
client = MongoClient(uri, server_api=ServerApi("1"))

db = client.library_management_system
collection = db["students"]
