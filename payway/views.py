from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from payway.serializers import PaywayLogSerializer
from rest_framework import status
from .models import paywaylog

from django.http import HttpResponse


# Create your views here.
class paywaylogview(APIView):
    def get(self, request):
        equationlogs = paywaylog.objects.all()
        serializer = PaywayLogSerializer(equationlogs, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaywayLogSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
