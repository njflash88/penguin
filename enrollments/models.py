from django.db import models
from datetime import datetime
from students.models import Student
from courses.models import Course

# Create your models here.
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    course  = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    passed = models.BooleanField(default=False)
    withdrawn = models.DateField()

def __str__(self):
        return self.title