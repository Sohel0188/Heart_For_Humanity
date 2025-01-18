from rest_framework import serializers
from . import models

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PostModel
        fields = '__all__'