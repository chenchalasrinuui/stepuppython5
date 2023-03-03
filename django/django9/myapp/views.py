from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from . import models
import json
# Create your views here.

@api_view(["GET"])
def getUsers(request):
    try:
        students=models.Student.objects.all().values()
        return HttpResponse(str(list(students)))
    except Exception as e:
        print(e)
        return HttpResponse(str(e))


@api_view(["POST"])  
def saveUser(request):
    try:
        data= json.loads(request.body)
        std = models.Student(name=data['name'], rno=data["rno"]) # create new model instance
        result=std.save() #seve to db
        print(result)
        return HttpResponse(result)
    except Exception as e:
        print(e)
        return HttpResponse(str(e))
