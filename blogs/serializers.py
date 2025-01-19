from rest_framework import serializers
from . import models

class BlogCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PostCategoryModel
        fields = '__all__'
        
class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PostModel
        fields = '__all__'

class BlogCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Post_Commernts
        fields = '__all__'
