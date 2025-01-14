from django.db import models

# Create your models here.
class PostModel(models.Model):
    post_title = models.CharField(max_length=255)
    post_slug = models.models.SlugField(max_length=255)
    