from django.db import models
from django.contrib.auth.models import User
from account.models import UserAccount

# Create your models here.
class Campain_Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)
    image = models.ImageField(upload_to='./media/campain/')
    def __str__(self):
        return self.title
    
class Campain (models.Model):
    campain_title = models.CharField(max_length=250,default="-")
    campain_slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Campain_Category,on_delete= models.CASCADE)
    image = models.ImageField(upload_to='./media/campain/')
    short_details = models.CharField(max_length=255)
    details = models.TextField()
    goal_price = models.FloatField()
    raised_price = models.FloatField()
    campain_day = models.IntegerField()
    donar = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
         