from re import finditer


pattern="^[0-9]{10}$"

input="012345678955"

result=finditer(pattern,input)
resList=list(result)
print(len(resList))
for v in resList:
    print(v)

