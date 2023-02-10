#Exception Handling

def f1():
    print('start')
    no1=10
    no2=0
    print(1)
    try:
        print(int('sachin'))
        print(no1/no2)
   
    except (ValueError, TypeError,ZeroDivisionError) as e:
        print(type(e))
        print(e)
        no2=1
    except BaseException as e:
        print('Base', type(e))
        print(e)
        no2=1
    print(2)
    print(no1/no2)
    print('end')
f1()