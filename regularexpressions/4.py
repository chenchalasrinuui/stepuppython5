#[abc]

from re import findall 
pattern="[^a-zA-Z0-9\s]"
input="df_dj a djflkdjl b 3er$kj"
result=findall(pattern,input)
print(result)

