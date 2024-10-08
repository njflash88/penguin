from django.db import models
from django.contrib.auth import get_user_model
#from .models import Course
# Get the custom User model
User = get_user_model()

# Create your models here.
class Forum(models.Model):
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=150,blank=True)
    keywords = models.CharField(max_length=150,blank=True)
    message = models.CharField(max_length=500,blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    purge = models.BooleanField(default=False)
    post_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE )
    content = models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.forum.title