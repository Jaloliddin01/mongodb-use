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

production = client.production
person_collection = production.person_collection

def create_documents():
    first_name = ['Tim', 'Sarah', 'Jennifer', 'Jose', 'Brad', 'Allen']
    last_name = ['Ruscica', 'Smith', 'Bart', 'Cater', 'Pit', 'Geral']
    age = [21, 40, 23, 19, 34, 67]

    for first_name, last_name, age in zip(first_name, last_name, age):
        doc = {'first_name': first_name, 'last_name': last_name, 'age': age}
        person_collection.insert_one(doc)
    