from django.db import models
import datetime

# Create your models here.

# Create a Student table in the database with the following fields
class Student(models.Model):
	w_num = models.CharField(max_length=8)
	in_time = models.TimeField()
	out_time = models.TimeField(null=True)
	date = models.DateField(auto_now_add=True)