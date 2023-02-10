import pymongo 
try:
    url="mongodb://localhost:27017"
    mongoClient=pymongo.MongoClient(url)
    db=mongoClient["school"]
    collection=db["students"]
    docs=[
        {
            "name":"s6","rno":"6","address":"Hyd"
        },
        {
            "name":"s7","rno":"7","address":"Hyd"
        }
    ]
    result=collection.insert_many(docs)
    if (result.acknowledged and result.inserted_ids):
        print("Inserted successfully")
    else:
        print("Not Inserted, try again")
except Exception as e:
    print(e)