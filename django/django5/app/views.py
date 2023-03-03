from django.shortcuts import render,HttpResponse

# Create your views here.


def getUsers(request):
    name=request.GET["n"]
    loc=request.GET["l"]
    data={
        "name":name,
        "location":loc
    }
    #return HttpResponse("Hellow...")
    return render(request,'wish.html', context=data)
    render()

