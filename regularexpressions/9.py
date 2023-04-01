from re import finditer

pattern="^([a-z]+[0-9]*@[a-z]+\.[a-z]{2,3})$"

input="abcd111@gmail.com"

result=finditer(pattern,input)
resList=list(result)
print(len(resList))
for v in resList:
    print(v)

