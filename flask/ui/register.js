function fnRegister(){
 var nameRef=document.getElementById('name')
 var uidRef=document.getElementById('uid')
 var pwdRef=document.getElementById('pwd')
 var rnoRef=document.getElementById('rno')
 var addRef=document.getElementById('add')
 var resRef=document.getElementById('result')

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

// AJAX

// create obj fro XMLHttpRequest class 

var obj=new XMLHttpRequest()

// prepare the request 

obj.open("POST",'http://127.0.0.1:5000/std-reg')

//Add request header

obj.setRequestHeader('Content-Type','application/json')

// send the request 

obj.send(JSON.stringify(data))

// receive the req and processing the req : server app 

//handle success response 
obj.onload=function(){
    var res=obj.responseText;
    resRef.innerText=res;
    nameRef.value =''
    uidRef.value =''
    pwdRef.value =''
    rnoRef.value =''
    addRef.value=''
}

// handle failure response

obj.onerror=function(){
    var res=obj.responseText;
    resRef.innerText=res;
}





}

