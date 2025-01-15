from rest_framework import serializers
from . import models

class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.About_us
        fields = '__all__'