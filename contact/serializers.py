from rest_framework import serializers
from . import models

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Contact_info
        fields = '__all__'
        
class ContactFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Contact_form
        fields = '__all__'