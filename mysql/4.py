import mysql.connector as con

try:
    dbObj=con.connect(host='localhost',user="root",password="root", database="school")
    cursorObj=dbObj.cursor()
    query="update students set rno=3333 where name='s1'"
    cursorObj.execute(query)
    dbObj.commit()
    print(cursorObj.rowcount, 'row(s) affected')
    print('success')
except Exception as e:
    print(e)
finally:
    print('finally')
    dbObj.close()