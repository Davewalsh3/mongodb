import pymongo
import os
if os.path.exists("env.py"):
    import env


MONGODB_URI = os.environ.get("MONGODB_URIs")

DBS_NAME = "mytestdatabase"

COLLECTION_NAME = "myfirstmdb"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print(" Oh, what a day... what a lovely day!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour':
                 'maroon'}})

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)
