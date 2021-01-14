from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Country, City, District, Temperature, Humidity, Pressure, Wind, Precipitation, Precipitation_icon, Cloud, Cloudy_icon, Day
from .serializers import WeatherSerializer

def index(request):
    country_list = Country.objects.all()
    city_list = City.objects.all()
    district_list = District.objects.all()
    return render(request, 'weather/list.html',  {'country_list' : country_list, 'city_list' : city_list, 'district_list' : district_list})

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
