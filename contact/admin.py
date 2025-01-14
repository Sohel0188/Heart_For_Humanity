from django.contrib import admin
from . import models

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','subject']
    
class Contact_info_Admin(admin.ModelAdmin):
    list_display = ['address','phone']
    
admin.site.register(models.Contact_info,Contact_info_Admin)

admin.site.register(models.Contact_form,ContactAdmin)


