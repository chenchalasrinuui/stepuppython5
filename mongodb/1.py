import pymongo #pip in pymongo

#print(type(pymongo))

#print(dir(pymongo))
try:
        #url='mongodb://localhost:27017'
        #url="mongodb+srv://su:su@cluster1.eccp0ho.mongodb.net/?retryWrites=true&w=majority"
        url='mongodb+srv://stepup:stepup@cluster0.eyocnzx.mongodb.net/?retryWrites=true&w=majority'
        mongoClient=pymongo.MongoClient(url)
        db=mongoClient["school"]
        collection=db["students"]
        data={"name":"s1","rno":1,"address":"Hyd"}

        result=collection.insert_one(data)

        #print(dir(result))

        if (result.acknowledged and result.inserted_id):
            print("Inserted successfully")
        else:
            print("Not Inserted, try again")
except BaseException as e:
        print("Exception raised")
        print(e)
finally:
        print("finally block excuted")


