from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

USER_TYPE=[
    ("admin","admin"),
    ("donar","donar"),
    ]
class UserAccount(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='./media/profile/',null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default="donar")
    # pyis_active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.author.username}"

        
