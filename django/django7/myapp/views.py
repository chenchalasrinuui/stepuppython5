from django.shortcuts import render, HttpResponse
import json
# Create your views here.


def fnQueryParams(request):
    data=request.GET
    return HttpResponse("My name is {}, I am from {}".format(data["n"],data["l"]))

def fnPathParams(request,n,l):
    return HttpResponse("My name is {}, I am from {}".format(n,l))

def fnRequestHeaders(request):
    print(request.headers)
    return HttpResponse("My name is {}, I am from {}".format(request.headers["Name"],request.headers["Loc"]))

def fnRequestBody(request):
    data=json.loads(request.body)
    return HttpResponse("My name is {}, I am from {}".format(data["name"],data["loc"]))
    

