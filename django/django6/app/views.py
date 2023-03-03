from django.shortcuts import render,HttpResponse

# Create your views here.

def fnHome(request):
     #return HttpResponse("Home")
     return render(request,'home.html')
def fnAbout(request):
     #return HttpResponse('About')
     return render(request,'about.html')
def fnContact(request):
    #return HttpResponse('Contact')
    return render(request,'contact.html')

