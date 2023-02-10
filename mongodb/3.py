import pymongo 
try:
    url="mongodb://localhost:27017"
    mongoClient=pymongo.MongoClient(url)
    db=mongoClient["school"]
    collection=db["students"]
    docs=[
        {
            "_id":1,"name":"s8","rno":"8","address":"Hyd"
        },
        {
          "_id":2,  "name":"s9","rno":"9","address":"Hyd"
        }
    ]
    result=collection.insert_many(docs)
    if (result.acknowledged and result.inserted_ids):
        print("Inserted successfully")
    else:
        print("Not Inserted, try again")
except Exception as e:
    print(e)