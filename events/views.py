from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializers
    
class EventBookingViewSet(viewsets.ModelViewSet):
    queryset = models.EventBooking.objects.all()
    serializer_class = serializers.EventBookingSerializers

