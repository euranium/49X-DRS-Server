from django.db import models
from django.db.models import Avg
from datetime import timedelta

# Create your models here.

# Create a Student table in the database with the following fields
class Student(models.Model):
	w_num = models.CharField(max_length=8)
	in_time = models.DateTimeField()
	out_time = models.DateTimeField(null=True)
	total_time = models.IntegerField(null=True,blank=True,default=None)
	date = models.DateField(auto_now_add=True)
	
	def average(self, w_num, total_time):
		qs = self._default_manager.filter(w_num=w_num)
		avg = qs.aggregate(Avg('total_time'))
		return int(avg['total_time__avg'])
	def get_average(self):
		w_num = self.w_num
		total_time = self.total_time
		return self.average(w_num,total_time)
	get_average.short_description = 'Average Duration (Minutes)'
	def duration(self):
		return self.total_time
	duration.short_description = 'Duration (Minutes)'
