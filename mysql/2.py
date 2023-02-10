import mysql.connector as con;

try:
    dbObj=con.connect(host="localhost",user='root',password='root',database="school")
    myCursor=dbObj.cursor()
    query="select * from students"
    myCursor.execute(query)
    data=myCursor.fetchall()
    for d in data:
        print(d)
except Exception as e:
    print(e)
