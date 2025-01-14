from django.db import models

# Create your models here.

class About_us(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='./media/about_image/')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'About Us'