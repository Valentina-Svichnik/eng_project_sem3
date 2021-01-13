from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import New, Advertice
# from .serializers import AdverticeSerializer

def index(request):
    news_list = New.objects.all()
    advertices_list = Advertice.objects.all()
    return render(request, 'weather/list.html',  {'news_list' : news_list, 'advertices_list' : advertices_list})

class AdverticeView(APIView):
    def get(self, request):
        advertice = Advertice.objects.all()
        return Response({"advertice": advertice})