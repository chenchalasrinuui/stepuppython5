def f1():
    try:
        print(1)
        print(10/0)
        print(2)
    except:
        print('except')
    finally:
        print('finally')

f1()
