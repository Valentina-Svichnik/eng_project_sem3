from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_with_pivot, name='dashboard'),
    path('data', views.pivot_data, name='pivot_data'),
]