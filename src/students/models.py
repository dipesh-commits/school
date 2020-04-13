from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length = 120)
	roll_no = models.IntegerField()
	gender = models.CharField(max_length=120)
	dob = models.DateField(default = '1998-01-01')
	grade = models.IntegerField()
	father_name = models.CharField(max_length=120)
	timestamps = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now= True)

	def __str__(self):
		return self.name

