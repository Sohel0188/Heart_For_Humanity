from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.PostModel.objects.all()
    serializer_class = serializers.BlogSerializers