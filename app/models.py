from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length = 50)
    emp_id = models.AutoField(primary_key=True)
