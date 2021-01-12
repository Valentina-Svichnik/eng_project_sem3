from django.shortcuts import render

from .models import User

def index(request):
    users_list = User.objects.all()
    return render(request, 'weather/list.html',  {'users_list' : users_list})