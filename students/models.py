from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from students.choices import district_choices, countries_choices

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=50,choices=district_choices.items())
    country = models.CharField(max_length=50,choices=countries_choices.items())
    postal = models.CharField(max_length=20)
    start_date = models.DateField()
    em_contact_name = models.CharField(max_length=30)
    em_contact_tel = models.name = models.CharField(max_length=30)

def __str__(self):
    return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
