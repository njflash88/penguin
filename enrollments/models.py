from django.db import models
from datetime import datetime
from django.utils import timezone
from courses.models import Course
from django.contrib.auth import get_user_model
# Get the custom User model
User = get_user_model()

# Create your models here.
class Enrollment(models.Model):
    student = models.CharField(max_length=255)
    course  = models.CharField(max_length=30)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False, blank=True)
    finished = models.BooleanField(default=False, blank=True)
    passed = models.BooleanField(default=False, blank=True)
    withdrawn = models.DateField(blank=True, null=True)

 
    def __str__(self):
        return self.title