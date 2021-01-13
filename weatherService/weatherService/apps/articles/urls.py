from django.urls import path
from .views import AdverticeView


app_name = "advertices"

urlpatterns = [
    path('advertices/', AdverticeView.as_view()),
    path('advertices/<int:pk>', AdverticeView.as_view())
]