
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

from . import serializers
from . import models
# Create your views here.
class CampainCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Campain_Category.objects.all()
    serializer_class = serializers.CampainCategorySerializers
    
class CampainViewSet(viewsets.ModelViewSet):
    queryset = models.Campain.objects.all()
    serializer_class = serializers.CampainSerializers
    
    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.request.query_params.get('category')
        if slug :
            queryset = queryset.filter(slug=slug)
        return queryset

        
class DonetionViewSet(viewsets.ModelViewSet):
    queryset = models.Donate.objects.all()
    serializer_class = serializers.DonetionSerializers