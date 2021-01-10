from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"hello/index.html")
def lokesh(request):
    return render(request,"hello/index.html")
def lok(request):
    return HttpResponse("Hello lokesh")

def greet(request,name):
    return render(request,"hello/greet.html", {
        "name":name.capitalize()
    })

