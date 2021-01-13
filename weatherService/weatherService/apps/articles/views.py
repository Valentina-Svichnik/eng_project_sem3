from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import New, Advertice
from .serializers import AdverticeSerializer

def index(request):
    news_list = New.objects.all()
    advertices_list = Advertice.objects.all()
    return render(request, 'weather/list.html',  {'news_list' : news_list, 'advertices_list' : advertices_list})

class AdverticeView(APIView):
    def get(self, request):
        advertices = Advertice.objects.all()
        serializer = AdverticeSerializer(advertices, many=True)
        return Response({"advertices": serializer.data})

        def post(self, request):
            advertice = request.data.get('advertice')
            
            serializer = AdverticeSerializer(data=advertice)
            if serializer.is_valid(raise_exception=True):
                advertice_saved = serializer.save()
            return Response({"success": "Advertice '{}' created successfully".format(advertice_saved.subject)})

        def put(self, request, pk):
            saved_advertice = get_object_or_404(Advertice.objects.all(), pk=pk)
            data = request.data.get('advertice')
            serializer = AdverticeSerializer(instance=saved_advertice, data=data, partial=True)

            if serializer.is_valid(raise_exception=True):
                advertice_saved = serializer.save()

            return Response({
                "success": "Advertice '{}' updated successfully".format(advertice_saved.title)
            })