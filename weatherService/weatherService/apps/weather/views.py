from django.shortcuts import render

from .models import Country, City, District, Temperature, Humidity, Pressure, Wind, Precipitation, Precipitation_icon, Cloud, Cloudy_icon, Day

def index(request):
    users_list = User.objects.all()
    country_list = Country.objects.all()
    city_list = City.objects.all()
    district_list = District.objects.all()
    return render(request, 'weather/list.html',  {'users_list' : users_list, 'country_list' : country_list, 'city_list' : city_list, 'district_list' : district_list})


