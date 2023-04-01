from re import finditer

pattern="^([a-z]+@[a-z]+\.[a-z]{2,3})$"

input="abcd@gmail.com"

result=finditer(pattern,input)
resList=list(result)
print(len(resList))
for v in resList:
    print(v)

