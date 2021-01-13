from django.urls import path
from .views import AdverticeView
from . import views


app_name = "advertices"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('advertices/', AdverticeView.as_view()),
]