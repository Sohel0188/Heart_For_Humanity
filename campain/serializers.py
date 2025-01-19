from rest_framework import serializers
from . import models

class CampainCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Campain_Category
        fields = '__all__' 

class CampainSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Campain
        fields = '__all__'