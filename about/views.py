from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.
class AboutViewSet(viewsets.ModelViewSet):
    queryset = models.About_us.objects.all()
    serializer_class = serializers.AboutSerializers