class SalException(Exception):
    def __init__(self,name):
        self.name=name

sal=input('Enter Salary')
try:
    if(int(sal)< 0):
        raise SalException("Salary should be +ve") # obj.__init__(obj,"Salary should be +ve")
except BaseException as e:
    sal='0'
    print(e)
print('My salaray is '+sal)
print('End')