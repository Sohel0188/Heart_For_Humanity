
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact_info.objects.all()
    serializer_class = serializers.ContactSerializers
    
class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = models.Contact_form.objects.all()
    serializer_class = serializers.ContactFormSerializers