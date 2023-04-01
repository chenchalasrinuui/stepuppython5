#d,D,s, S, w, W 

from re import finditer 

pattern="\d{3}a"
input="abc 233a434 bcd 343434a"

result=finditer(pattern,input)

for v in result:
    print(v)
    print(v.start(),'...',v.end(),'....',v.group())

