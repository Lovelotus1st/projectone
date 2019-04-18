from django.db import models
#import datetime
from django.db import models
#from django.utils import timezone


# Create your models here.

class Login(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField()
    password = models.CharField(max_length=50)
    v_password = models.CharField(max_length=50)

    def __str__(self):
        return self.fname




# Create your models here.
