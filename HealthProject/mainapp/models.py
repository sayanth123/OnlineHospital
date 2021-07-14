from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True)
    available = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name



TIME_CHOICES = (
   ('10 AM - 1 PM', 'morning'),
   ('2 PM - 5 PM', 'afternoon')
)


class Patient(models.Model):
    name = models.CharField(max_length=250, unique=True)
    date = models.DateField()
    time = models.CharField(choices=TIME_CHOICES,max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    phone=models.CharField(max_length=50)
    message = models.CharField(max_length=300)

    def __str__(self):
        return  self.name

