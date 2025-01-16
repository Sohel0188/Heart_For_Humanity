from django.db import models
from account.models import UserAccount
# Create your models here.
class PostCategoryModel(models.Model):
    category_name = models.CharField(max_length=50)
    category_slug = models.SlugField(max_length=55)
    category_image = models.ImageField(upload_to='./media/post_image/', null=True, blank=True)
    
    def __str__(self):
        return self.category_name
    
class PostModel(models.Model):
    post_title = models.CharField(max_length=255)
    post_slug = models.SlugField(max_length=255)
    post_description = models.TextField(default="_")
    post_category = models.ForeignKey(PostCategoryModel, on_delete=models.CASCADE, related_name='category')
    post_image = models.ImageField(upload_to="./media/post_image/" )
    created_date = models.DateTimeField(auto_now_add=True)

class Post_Commernts(models.Model):
    commenter = models.ManyToManyField(UserAccount)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.commenter.username} {self.post.post_title} {self.comment}"
    

