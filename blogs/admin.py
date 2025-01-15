from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'post_slug':('post_title',),}
    list_display = ['post_title','post_category','post_description']

class PostCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug':('category_name',),}
    list_display = ['category_name']
    
admin.site.register(models.PostModel,PostAdmin)
admin.site.register(models.PostCategoryModel,PostCategoryAdmin)
