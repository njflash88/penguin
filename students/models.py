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
    username = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username', default='')
    last_name = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=50, default='')
    street = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=20, default='')
    district = models.CharField(default='',max_length=50,choices=district_choices.items())
    country = models.CharField(default='',max_length=50,choices=countries_choices.items())
    postal = models.CharField(max_length=20, default='')
    start_date = models.DateField(default=timezone.now)
    em_contact_name = models.CharField(max_length=30, default='', blank=True)
    em_contact_tel = models.name = models.CharField(max_length=30, default='', blank=True)

    def __str__(self):
        return self.user.user_name
