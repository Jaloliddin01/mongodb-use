from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
import urllib

load_dotenv(find_dotenv())

password = os.environ.get('MONGODB_PWD')

connection_string = f"mongodb+srv://vertow:" + urllib.parse.quote(password) + "@cluster0.m2tnsab.mongodb.net/?retryWrites=true&w=majority"
print(urllib.parse.quote(password))
client = MongoClient(connection_string)

dbs = client.list_database_names()
test_db = client.test
collections = test_db.list_collection_names()


def insert_test_doc():
    collection = test_db.test
    data = {
        'name': 'Tim',
        'type': 'Test',
    }
    id = collection.insert_one(data).inserted_id
    print(id)

insert_test_doc()