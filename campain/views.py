
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

from . import serializers
from . import models
# Create your views here.
class CampainCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Campain_Category.objects.all()
    serializer_class = serializers.CampainCategorySerializers
    lookup_field = 'slug'
    
class CampainViewSet(viewsets.ModelViewSet):
    queryset = models.Campain.objects.all()
    serializer_class = serializers.CampainSerializers
    lookup_field = 'campain_slug'
    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.request.query_params.get('category')  # Updated parameter name
        if slug:
            queryset = queryset.filter(category=slug)
        return queryset

        
class DonetionViewSet(viewsets.ModelViewSet):
    queryset = models.Donate.objects.all()
    serializer_class = serializers.DonetionSerializers