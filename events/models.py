from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    event_data = models.DateField()
    event_start_time = models.CharField(max_length=20)
    event_end_time = models.CharField(max_length=20)
    event_description = models.TextField()
    specker = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.title} {self.event_data}" 