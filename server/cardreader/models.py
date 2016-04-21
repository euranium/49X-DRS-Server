from django.db import models

# Create your models here.

# Create a Student table in the database with the following fields
class Student(models.Model):
    w_num = models.CharField(max_length=9)
    in_time = models.TimeField()
    out_time = models.TimeField()