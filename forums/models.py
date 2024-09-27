from django.db import models
from django.contrib.auth import get_user_model
#from .models import Course
# Get the custom User model
User = get_user_model()

# Create your models here.
class Forum(models.Model):
    created_by  = models.ForeignKey(User, on_delete=models.DO_NOTHING, to_field='username')
  #  course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, to_field='title')
    discussion_title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    poster = models.CharField(max_length=255)
    message = models.CharField(max_length=300)
    purge = models.BooleanField(default=False)

def __str__(self):
        return self.discussion_title