from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
flights=Flight.objects.all()
def index(request):
    return render(request,"flights/index.html",{
        "flights":flights
    })
def display(request,flight_id):
    flight=Flight.objects.get(pk=flight_id)
    return render(request,"flights/display.html",{
        "flight":flight
    })
