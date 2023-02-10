#Exception Handling

def f1():
    print('start')
    no1=10
    no2='sachin'
    print(1)
    try:
        print(no1/no2)
    except BaseException as e:
        print(type(e))
        print(e)
        no2=1
    print(2)
    print(no1/no2)
    print('end')
f1()