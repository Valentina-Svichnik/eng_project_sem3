from django.http import JsonResponse
from django.shortcuts import render
from articles.models import New
from django.core import serializers

def pivot_data(request):
    dataset = New.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def dashboard_with_pivot(request):
    return render(request, 'weather/dashboard.html', {})

