from rest_framework import serializers
from . import models

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'
        
class EventBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.EventBooking
        fields = '__all__'