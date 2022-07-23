from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is our homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is our about page")

def service(request):
    return render(request, 'service.html')
    #return HttpResponse("this is our service page")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("this is our contact page")
     
