from django.db import models

# Create your models here.
GENDER=[
    ("male","male"),
    ("female","female"),
    ]
class Volunteer(models.Model):
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=15)
	email = models.EmailField()
	gender = models.CharField(max_length=10, choices=GENDER)
	bio = models.TextField()
	profile_image = models.ImageField(upload_to='./media/profile/',null=True, blank=True)

	def __str__(self):
		return f"{self.name} {self.phone}"

