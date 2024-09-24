from django.db import models
#from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from students.choices import district_choices, countries_choices
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
# Get the custom User model
User = get_user_model()

# Create your models here. 
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=50,choices=district_choices.items())
    country = models.CharField(max_length=50,choices=countries_choices.items())
    postal = models.CharField(max_length=20)
    start_date = models.DateField(default=timezone.now)
    em_contact_name = models.CharField(max_length=30)
    em_contact_tel = models.name = models.CharField(max_length=30)

def __str__(self):
    return self.user.user_name
