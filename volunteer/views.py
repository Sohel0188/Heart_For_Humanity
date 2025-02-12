from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.
class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = models.Volunteer.objects.all()
    serializer_class = serializers.VolunteerSerializers