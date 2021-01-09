# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Привет мир")

from django.shortcuts import render
from .models import Weather, Comment

def index(request):
    weather_list = Weather
    return render(request, "weather/list.html")