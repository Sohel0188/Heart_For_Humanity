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

# class BlogCommentsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = models.Post_Commernts
#         fields = '__all__'

class BlogCommentsSerializers(serializers.ModelSerializer):
    commenter_name = serializers.SerializerMethodField()
    commenter_image = serializers.SerializerMethodField()
    class Meta:
        model = models.Post_Commernts
        fields = ['id', 'comment','commenter', 'commenter_name','commenter_image','post']

    def get_commenter_name(self, obj):
        return obj.commenter.author.username
        
    def get_commenter_image(self, obj):
        request = self.context.get('request') 
        if obj.commenter.profile_image: 
            return request.build_absolute_uri(obj.commenter.profile_image.url)
        return None


