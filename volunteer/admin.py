from django.contrib import admin
from . import models
# Register your models here.
class VolunteerAdmin(admin.ModelAdmin):
	admin.site.register(models.Volunteer)