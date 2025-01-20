from django.contrib import admin
from . import models
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ["title","event_data","event_start_time","event_end_time"]
    
class EventBookingAdmin(admin.ModelAdmin):
    list_display = ["name","email","phone"]

admin.site.register(models.Event,EventAdmin)
admin.site.register(models.EventBooking,EventBookingAdmin)
