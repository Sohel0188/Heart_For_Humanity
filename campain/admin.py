from django.contrib import admin
from . import models

# Register your models here.
class CampainCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',),}
    list_display = ["title"]

class CampainAdmin(admin.ModelAdmin):
    prepopulated_fields = {'campain_slug':('campain_title',),}
    list_display = ["campain_title","category","goal_price"]

class DonetionAdmin(admin.ModelAdmin):
    list_display = ['user',"name","email","phone","amount"]
    
admin.site.register(models.Campain_Category,CampainCategoryAdmin)
admin.site.register(models.Campain,CampainAdmin)
admin.site.register(models.Donate,DonetionAdmin)
