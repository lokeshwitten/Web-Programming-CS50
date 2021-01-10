from django.shortcuts import render
import datetime
from django.http import HttpResponse
def index(request):
    now=datetime.datetime.now()
    return render(request,"today/index.html")

