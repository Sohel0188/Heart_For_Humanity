
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
    serializer_class = serializers.CampainSerializers
    queryset = models.Campain.objects.all()
    lookup_field = 'campain_slug'
    def get_queryset(self):

        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        
        if category_id:
            queryset = queryset.filter(category=category_id)
        return queryset

class DonetionViewSet(viewsets.ModelViewSet):
    queryset = models.Donate.objects.all()
    serializer_class = serializers.DonetionSerializers
    def perform_create(self, serializer):
        donation = serializer.save()
        donar = donation.user
        campaign = donation.campaign

        print(donation.amount)
        if campaign:
            campaign.raised_price += donation.amount
            donar.total_donet_amount+=donation.amount
            print(donar)
            print(campaign)
            donar.save()
            campaign.save()

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user')

        if user_id :
            queryset = queryset.filter(user=user_id)
        return queryset