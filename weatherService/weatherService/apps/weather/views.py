from django.contrib.auth.forms import AuthenticationForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView


from .models import Country, City, District, Temperature, Humidity, Pressure, Wind, Precipitation, Precipitation_icon, Cloud, Cloudy_icon, Day, User
from .forms import AuthUserForm, RegisterUserForm
from .serializers import WeatherSerializer

def index(request):
    district_list = District.objects.all()
    cloud_list = Cloud.objects.order_by('-day')[:1]
    prec_icon = Precipitation_icon.objects.all()
    prec = Precipitation.objects.order_by('day')[:1]
    pressure_list = Pressure.objects.order_by('-day')[:1]
    temp_list = Temperature.objects.order_by('-day')[:1]
    wind_list = Wind.objects.order_by('-day')[:1]
    humidity_list = Humidity.objects.order_by('-day')[:1]
    return render(
        request,
        'weather/main.html',
        {
            'district_list' : district_list,
            'cloud_list' : cloud_list,
            'prec_icon' : prec_icon,
            'prec' : prec,
            'pressure_list' : pressure_list,
            'temp_list' : temp_list,
            'wind_list' : wind_list,
            'humidity_list' : humidity_list
        }
    )

def news(request):
    return render(
        request,
        'weather/news.html'
    )

def map(request):
    return render(
        request,
        'weather/map.html'
    )    

def archive(request):
    country_list = Country.objects.all()
    city_list = City.objects.all()
    district_list = District.objects.all()
    icon_list = Precipitation_icon.objects.all()
    return render(request, 'weather/archive.html',  {'country_list' : country_list, 'city_list' : city_list, 'district_list' : district_list, 'icon_list' : icon_list})

class LoginView(LoginView):
    template_name = 'weather/login.html'
    form_class = AuthUserForm
    success_url = '/'
    model = User
    success_msg = 'Пользователь успешно создан'
    def get_success_url(self):
        return self.success_url

    
class RegistrateView(CreateView):
    template_name = 'weather/registrate.html'
    form_class = RegisterUserForm
    success_url = '/'
    model = User
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username = username, password = password)
        login(self.request, auth_user)
        return form_valid


class Logout(LogoutView):
    next_page = '/'

class WeatherView(APIView):
    def get(self, request):
        weather = Day.objects.all()
        serializer = WeatherSerializer(weather, many=True)
        return Response({"weather": serializer.data})

        def post(self, request):
            weather = request.data.get('weather')
            
            serializer = WeatherSerializer(data=weather)
            if serializer.is_valid(raise_exception=True):
                weather_saved = serializer.save()
            return Response({"success": "Day '{}' created successfully".format(weather_saved.date)})

        def put(self, request, pk):
            saved_weather = get_object_or_404(Day.objects.all(), pk=pk)
            data = request.data.get('weather')
            serializer = WeatherSerializer(instance=saved_weather, data=data, partial=True)

            if serializer.is_valid(raise_exception=True):
                weather_saved = serializer.save()

            return Response({
                "success": "Day '{}' updated successfully".format(weather_saved.date)
            })


