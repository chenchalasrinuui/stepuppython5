from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
import json
# Create your views here.

@api_view(["GET"])
def fnTestGetQuery(request):
    name=request.GET["name"]
    loc=request.GET["loc"]
    return HttpResponse(name+"..."+loc)

@api_view(["PUT"])
def fnTestPutPath(request,name,loc):
     return HttpResponse(name+"..."+loc)

@api_view(["POST"])
def fnTestPostBody(request):
     data=json.loads(request.body)
     name=data["name"]
     loc=data["loc"]
     return HttpResponse(name+"..."+loc)

@api_view(["DELETE","PATCH"])
def fnTestDelHeader(request):
     name=request.headers["name"]
     loc=request.headers["loc"]
     return HttpResponse(name+"..."+loc)