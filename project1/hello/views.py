from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    render(request,"hello/index.html")
def lokesh(request):
    return HttpResponse("Hello lokesh")
def lok(request):
    return HttpResponse("Hello lokesh")

def greet(request,name):
    return HttpResponse(f"Hello {name.capitalize()}!!")
