from rest_framework import serializers
from . import models

class CampainCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Campain_Category
        fields = '__all__' 

class CampainSerializers(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Campain
        fields = [
            'id',
            'campain_title',
            'campain_slug',
            'image',
            'short_details',
            'details',
            'goal_price',
            'raised_price',
            'campain_day',
            'category',  # Keeps the ID
            'category_name',  # Adds the name
        ]

    def get_category_name(self, obj):
        return obj.category.title
    
class DonetionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Donate
        fields = '__all__'
        