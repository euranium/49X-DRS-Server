from django.contrib import admin
from cardreader.models import Student

def sort_st(modeladmin):
	str("test")
sort_st.short_description = "test"

class StudentAdmin(admin.ModelAdmin):
	readonly_fields = ('date',)
	list_display = ('w_num','date','in_time','out_time','duration','get_average')
	ordering = ('date',)
	actions = [sort_st]
	search_fields = ('w_num','date',)
	list_filter = ('date',)
admin.site.register(Student,StudentAdmin)
# Register your models here.

