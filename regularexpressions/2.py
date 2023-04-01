from re import finditer,fullmatch

pattern="abc"
input="dajfldjfldeb abc rejljc ejlrej"

result=finditer(pattern,input)
for val in result:
    print(val.group())

