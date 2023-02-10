import pymongo;

try:
    url="mongodb://localhost:27017"
    #url='mongodb+srv://stepup:stepup@cluster0.eyocnzx.mongodb.net/?retryWrites=true&w=majority'
    mongoClient=pymongo.MongoClient(url)
    db=mongoClient["school"]
    collection=db["students"]
    #result=collection.find()
    for val in collection.find({},{'_id':0}):
        print(val)
except Exception as e:
    print(e)