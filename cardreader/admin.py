from django.contrib import admin
from cardreader.models import Student

class StudentAdmin(admin.ModelAdmin):
	readonly_fields = ('date',)
	list_display = ('w_num','date','in_time','out_time','duration','get_average','logged_out','note')
	ordering = ('date',)
	search_fields = ('w_num','date',)
	list_filter = ('date',)
admin.site.register(Student,StudentAdmin)
# Register your models here.
