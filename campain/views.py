
from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.
class CampainCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Campain_Category.objects.all()
    serializer_class = serializers.CampainCategorySerializers
    
class CampainViewSet(viewsets.ModelViewSet):
    queryset = models.Campain.objects.all()
    serializer_class = serializers.CampainSerializers
    
class DonetionViewSet(viewsets.ModelViewSet):
    queryset = models.Donate.objects.all()
    serializer_class = serializers.DonetionSerializers