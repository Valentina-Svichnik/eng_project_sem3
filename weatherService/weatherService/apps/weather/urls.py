from django.urls import path 
from .views import WeatherView

from . import views

app_name = "weather"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('news/', views.news, name = 'news'),
    path('map/', views.map, name = 'map'),
    path('archive/', views.archive, name = 'archive'),
    path('weather/', WeatherView.as_view()),
    # path('weather/<int:pk>', WeatherView.as_view())
]