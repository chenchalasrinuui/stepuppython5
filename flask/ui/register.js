function fnRegister(){
 var nameRef=document.getElementById('name')
 var uidRef=document.getElementById('uid')
 var pwdRef=document.getElementById('pwd')
 var rnoRef=document.getElementById('rno')
 var addRef=document.getElementById('add')

 var name=nameRef.value 
 var uid=uidRef.value 
 var pwd=pwdRef.value 
 var rno=rnoRef.value 
 var add=addRef.value

 var data={
    "name":name,
    "uid":uid,
    "pwd":pwd,
    "rno":rno,
    "add":add
}
console.log(data)
}

