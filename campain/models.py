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
    
    def __str__(self):
        return f"{self.campain_title} {self.category} {self.campain_day} {self.goal_price} {self.raised_price}"

class Donate(models.Model):
    user = models.ForeignKey(UserAccount,default=0,null=True, blank=True, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campain,default=None,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    amount = models.FloatField()
    
    def __str__(self):
        user_info = self.user.author.username if self.user else "Guest User"
        return f"{user_info} {self.name} {self.email} {self.phone} {self.amount}"