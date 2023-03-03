from django.shortcuts import render, HttpResponse

# Create your views here.

def wish(request):
    #return HttpResponse('app2/wish.html')
    return render(request,'app2/wish.html')
