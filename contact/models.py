from django.db import models

# Create your models here.
class Contact_info(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    facebook_link = models.URLField()
    youtube_link = models.URLField()
    linkedIn_link = models.URLField()
    map = models.TextField()
    
    def __str__(self):
        return f"{self.address} {self.phone}"
    
    class Meta:
        verbose_name_plural = "Contact Information"

class Contact_form(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    contact_for = models.TextField()
    
    def __str__(self):
        return f"{self.name} {self.phone} {self.email}"
    
    class Meta:
        verbose_name_plural = "Contact Form"
    