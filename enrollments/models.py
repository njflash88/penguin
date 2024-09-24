from django.db import models
from datetime import datetime
from courses.models import Course
from django.contrib.auth import get_user_model
# Get the custom User model
User = get_user_model()

# Create your models here.
class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course  = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    passed = models.BooleanField(default=False)
    withdrawn = models.DateField(default='')

def __str__(self):
        return self.title