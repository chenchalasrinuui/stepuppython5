import pymongo

try:
    url="mongodb://localhost:27017"
    monogoClient=pymongo.MongoClient(url)
    db=monogoClient['school']
    collection=db['students'] 
    query={"address":'Hyderabad'}
    result=collection.delete_many(query)
    if(result.acknowledged and result.deleted_count > 0):
        print('Successfully Delete')
    else: 
        print('Not Deleted')
    #print(type(result))
    #print(dir(result))
    #print(result)
except Exception as e:
    print(e)
finally:
    print('finally')