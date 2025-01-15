from django.contrib import admin
from . import models
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","user_type"]
    def first_name(self,obj):
        return obj.author.first_name
    def last_name(self,obj):
        return obj.author.last_name
    
admin.site.register(models.UserAccount,UserAdmin)