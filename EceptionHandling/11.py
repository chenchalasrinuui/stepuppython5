class InvalidAge(BaseException):
    def __init__(self,name):
        self.name=name 
    

from sys import argv 


try:
    age=argv[1]
    if(int(age) < 18):
        raise InvalidAge('You are not eligible to register for voting')
    else:
        print('You are eligible')
except InvalidAge as e:
    print('Invalid')
    print(e)
except BaseException as e:
    print("Base")
    print(e)


print('end')