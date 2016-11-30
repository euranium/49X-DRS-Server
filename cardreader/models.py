from django.db import models
from django.db.models import Avg
import datetime

# Create your models here.

# Create a Student table in the database with the following fields
class Student(models.Model):
	w_num = models.CharField(max_length=8)
	in_time = models.DateTimeField()
	out_time = models.DateTimeField(null=True)
	date = models.DateField(auto_now_add=True)
	duration = models.IntegerField(null=True, blank=True, default=0)
	note = models.CharField(max_length=256, editable=True, default='')


	def average(self, w_num, duration):
		qs = Student.objects.filter(w_num=w_num,duration__gt=0)
		avg = qs.aggregate(Avg('duration'))
		return int(avg['duration__avg'])
	def get_average(self):
		w_num = self.w_num
		duration = self.duration
		return self.average(w_num,duration)
	get_average.short_description = 'Average Duration (Minutes)'
