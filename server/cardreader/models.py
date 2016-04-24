from django.db import models

# Create your models here.

# Create a Student table in the database with the following fields
class Student(models.Model):
	def __unicode__(self):
		return format(self.w_num) + '-' + format(self.date)
	w_num = models.CharField(max_length=9)
	in_time = models.TimeField()
	out_time = models.TimeField(null=True)
	date = models.DateField(auto_now_add=True)
