from time import timezone
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from .serializers import *
from django.utils import *

class GetAllAPIView(APIView):
    def get(self, request):
        objects = Record.objects.all()
        data = []
        for obj in objects:
            data.append(RecordsSerializer(obj).data)
        return JsonResponse(data, safe=False)

class AddRecordAPIView(APIView):
    def post(self, request):
        record = Record()
        record.moist_1 = request.POST.get('moist_1')
        record.moist_2 = request.POST.get('moist_2')
        record.temp = request.POST.get('temp')
        record.rain = request.POST.get('rain')
        record.timestamp = timezone.now()
        record.save()
        return JsonResponse(RecordsSerializer(record).data, safe=False)
