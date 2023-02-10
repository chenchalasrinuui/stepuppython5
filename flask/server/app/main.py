from flask import Flask,request
import pymongo;
app = Flask(__name__)

@app.route('/std-reg',methods=['POST'])
def fnRegStd():
    try:
        data=request.json
        url='mongodb://localhost:27017'
        mongoClient=pymongo.MongoClient(url)
        db=mongoClient["school"]
        collection=db["students"]
        result=collection.insert_one(data)
        if (result.acknowledged and result.inserted_id):
            return "Inserted successfully"
        else:
            return "Not Inserted, try again"
    except BaseException as e:
            print("Exception raised")
            print(e)
            return e
    finally:
            print("finally block excuted")
       

@app.route('/std-reg-query',methods=['GET'])
def fnRegQuery():
    n=request.args.get('name')
    l=request.args.get('loc')
    return "Hellow This is {}, I am from {}".format(n,l)

@app.route('/std-reg-pathparams/<name>/<loc>',methods=['POST','GET'])
def fnRegPath(name,loc):
    return "Hellow This is {}, I am from {}".format(name,loc)

@app.route('/std-reg-headers',methods=['PUT','DELETE'])
def fnRegHeader():
    n=request.headers["name"]
    l=request.headers["loc"]
    return "Hellow This is {}, I am from {}".format(n,l)

@app.route('/std-reg-body',methods=['POST'])
def fnRegBody():
    n=request.json["name"]
    l=request.json["loc"]
    return "Hellow This is {}, I am from {}".format(n,l)



