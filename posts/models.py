from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    tags = TaggableManager()
    timestamp = models.DateField(auto_now_add=True)
    private_status = models.BooleanField(default=False)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    timestamp_edited = models.DateField(auto_now=True)
