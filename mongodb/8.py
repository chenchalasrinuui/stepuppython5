import pymongo

try:
    url="mongodb://localhost:27017"
    monogoClient=pymongo.MongoClient(url)
    db=monogoClient['school']
    collection=db['students']
    query={"address":"Hyd"}
    newData={"address":"Hyderabad"}
    result=collection.update_many(query,{"$set":newData})
    if(result.acknowledged and result.modified_count>0):
        print('Successfully Updated')
    else:
        print("Not Updated")
except Exception as e:
    print(e)
finally:
    print('finally')
