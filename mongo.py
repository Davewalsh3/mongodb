import pymongo
import os
from os import path
if path.exists("env.py"):
    import env


MONGODB_URI = os.environ.get("MONGODB_URIs")
DBS_NAME = "mytestdatabase"
COLLECTION_NAME = "myfirstmdb"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour':
 'grey', 'occupation': 'writer', 'nationality': 'english'}

documents = coll.find()

for doc in documents:
    print(doc)

    