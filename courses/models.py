from django.db import models
from django.shortcuts import render
from datetime import datetime
from instructors.models import Instructor

# Create your models here.

class Course(models.Model):
 #   id = models.CharField(max_length=10)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30)
    catagory = models.CharField(max_length=20)
    keyword = models.CharField(max_length=50)
    price = models.IntegerField()
    prerequisite = models.CharField(max_length=10)
    deadline = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    current_enrollment = models.BigIntegerField(default=0)
    max_enrollment = models.BigIntegerField(default=0)
    location = models.CharField(max_length=15, blank=True)


    def __str__(self):
        return self.title