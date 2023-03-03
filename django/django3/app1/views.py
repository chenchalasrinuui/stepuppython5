from django.shortcuts import render, HttpResponse

# Create your views here.

def wish(request):
    #return HttpResponse('app1/wish.html')
    return render(request,'app1/wish.html')
