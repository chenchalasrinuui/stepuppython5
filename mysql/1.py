import mysql.connector as con  # pip install mysql-connector-python
try:
    dbObj=con.connect(host='localhost',user="root",password="root", database="school")
    #print(type(dbObj))
    #print(dir(dbObj))
    #print(type(dbObj.cursor))
    myCursor=dbObj.cursor()
    #print(type(myCursor))
    #print(dir(myCursor))
    query="insert into students values (%s,%s,%s)"
    values=("s2",3,"Pune")
    result=myCursor.execute(query,values)
    dbObj.commit()
    print(result)
    print("success")
    
except Exception as e:
    print('error')
    print(e)
finally:
    print('finally')





