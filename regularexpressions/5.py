#d,D,s, S, w, W 

from re import search 

pattern="[abc]"
input="djfldkj abc jldkjflkd abc"

result=search(pattern,input)

print(result)