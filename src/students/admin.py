from django.contrib import admin

from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	readonly_fields = ['updated','timestamps']
	list_display = ['name','grade','dob']
	class Meta:
		model = Student



admin.site.register(Student)
