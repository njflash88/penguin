from django.db import models

# Create your models here.
class Emaillist(models.Model):
    email = models.CharField(max_length=30)
    name  = models.CharField(max_length=30)
    subscribe_date = models.DateTimeField(auto_now_add=True)
    purge = models.BooleanField(default=False)

def __str__(self):
        return self.email