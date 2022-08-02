from django.db import models
from django.urls import reverse

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=12) 
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    Address = models.CharField(max_length=150)
    division = models.CharField(max_length=50)
    date = models.DateField(null=True)
    image = models.ImageField(upload_to="image", null=True)

    def __str__(self):
        return f"{self.first_name}"
