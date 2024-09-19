from django.db import models
from students.models import district_choices, countries_choices

# Create your models here.
class Instructor(models.Model):
    #id = models.CharField(max_length=10)
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
    background = models.CharField(max_length=200)
    em_contact = models.CharField(max_length=30)
    em_tel = models.name = models.CharField(max_length=30)

    def __str__(self):
        return (self.firstname+" "+self.lastname)