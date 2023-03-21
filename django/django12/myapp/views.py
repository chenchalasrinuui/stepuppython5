from django.shortcuts import render
from rest_framework.decorators import api_view
import json;
from .serializers import StudentsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Student
# Create your views here.


@api_view(['GET'])
def fnGetUsers(request):
    try:
        students =  Student.objects.all().values()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"error":e})

@api_view(['POST'])
def fnSaveUser(request):
    try:
        dataObj = json.loads(request.body)
        stdSerializer=StudentsSerializer(data=dataObj)
        if stdSerializer.is_valid():
            stdSerializer.save()
            return Response({"status":200,"msg":"success"}, status=status.HTTP_201_CREATED)
        return Response("Not Inserted", status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("POST",e)
        return Response({"errro":e})

@api_view(['PUT','PATCH'])
def fnUpdateUser(request):
    try:
        obj=Student.objects.get(id = request.headers["id"])
        data = json.loads(request.body)
        stdSerializer=StudentsSerializer(obj,data=data)
        if stdSerializer.is_valid():
            stdSerializer.save()
            return Response("Success", status=status.HTTP_200_OK)
        return Response("Not Updated", status=status.HTTP_400_BAD_REQUEST)
    except BaseException as e:
        print("PUT",e)
        return Response({"error":e}) 
@api_view(['DELETE'])
def fnDeleteUser(request):
    try:
        obj=Student.objects.get(id = request.GET["id"])
        obj.delete()
        return Response("Success", status=status.HTTP_200_OK)
    except BaseException as e:
        print(e)
        return Response({"error":e})