from django.shortcuts import render, HttpResponse
from .models import Student
import json
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def fnGetUsers(request):
    try:
        students=Student.objects.all().values()
        return HttpResponse(str(list(students)))
    except Exception as e:
        print(e)
        return HttpResponse(str(e))

@api_view(['POST'])
def fnSaveUser(request):
    try:
        data=json.loads(request.body)
        std =Student(name=data['name'], rno=data["rno"]) # create new model instance
        result=std.save() 
        return HttpResponse(result)
    except Exception as e:
        print(e)
        return HttpResponse(str(e))

