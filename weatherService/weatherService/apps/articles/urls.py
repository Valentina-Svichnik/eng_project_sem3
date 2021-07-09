from django.urls import path
from .views import AdverticeView

from . import views

app_name = "advertices"

urlpatterns = [
    path('', views.adv, name = 'adv'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name = 'news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name = 'news-delete'),
    path('advertices/', AdverticeView.as_view()),
    path('advertices/<int:pk>', AdverticeView.as_view())
]