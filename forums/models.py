from django.db import models
from students.models import Student

# Create your models here.
class Forum(models.Model):
    created_by  = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    poster = models.CharField(max_length=30)
    message = models.CharField(max_length=300)
    purge = models.BooleanField(default=False)

def __str__(self):
        return self.title