from rest_framework import serializers
from . import models

class VolunteerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Volunteer
        fields = '__all__'