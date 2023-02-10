import pymongo

try:
    url="mongodb://localhost:27017"
    monogoClient=pymongo.MongoClient(url)
    db=monogoClient['school']
    collection=db['students'] 
    collection.drop()
except Exception as e:
    print(e)
finally:
    print('finally')