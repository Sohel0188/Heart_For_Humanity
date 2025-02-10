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
    campaign_title = serializers.SerializerMethodField()

    class Meta:
        model = models.Donate
        fields = '__all__'
        extra_fields = ['campain_name']
    def get_campaign_title(self, obj):
        return obj.campaign.campain_title if obj.campaign else None 
        