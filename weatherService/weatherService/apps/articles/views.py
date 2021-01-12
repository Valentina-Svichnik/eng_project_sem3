from django.shortcuts import render

from .models import New, Advertice

def index(request):
    news_list = New.objects.all()
    advertices_list = Advertice.objects.all()
    return render(request, 'weather/list.html',  {'news_list' : news_list, 'advertices_list' : advertices_list})

