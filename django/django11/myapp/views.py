from django.shortcuts import render,HttpResponse
from .models import Student
import json
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getUsers(request):
    try:
        result=Student.objects.all().values()
        return HttpResponse(str(list(result)))
    except Exception as e:
        print(e)
        return HttpResponse(str(e))
    
@api_view(['POST'])
def saveUser(request):
    try:
        data=json.loads(request.body)
        stdObj=Student(name=data['name'],rno=data['rno'])
        result=stdObj.save()
        return HttpResponse(result)
    except Exception as e:
        print(e)
        return HttpResponse(str(e))
   
