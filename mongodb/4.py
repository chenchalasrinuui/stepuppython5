import pymongo;

try:
    url="mongodb://localhost:27017"
    mongoClient=pymongo.MongoClient(url)
    db=mongoClient["school"]
    collection=db["students"]
    result=collection.find()
    for val in result:
        print(val)
except Exception as e:
    print(e)