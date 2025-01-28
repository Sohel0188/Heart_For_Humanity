from rest_framework import serializers
from . import models

class BlogCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PostCategoryModel
        fields = '__all__'
        
class BlogSerializers(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = models.PostModel
        fields = [
            'id',
            'post_title',
            'post_slug',
            'post_description',
            'post_image',
            'created_date',
            'post_category',
            'category_name',
        ]
    def get_category_name(self, obj):
        return obj.post_category.category_name

class BlogCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Post_Commernts
        fields = '__all__'
