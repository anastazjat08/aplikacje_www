from django.db import models

# Create your models here.


class Conference(models.Model):
	name = models.CharField(max_length=200, unique=True)
	place = models.CharField(max_length=500)
	start_date = models.DateField()
	end_date = models.DateField()
	abstract_deadline = models.DateField()

	def __str__(self):
		return f"{self.name}"

class Abstract(models.Model):
	conference = models.ForeignKey(Conference, on_delete=models.PROTECT) 
	title = models.CharField(max_length=200, unique=True)
	text = models.TextField()
	type_a = models.CharField(max_length=200,choices=[("PLAKAT", "PLAKAT"), ("REFERAT", "REFERAT"), ("REFERAT LUB PLAKAT", "REFERAT LUB PLAKAT")])
	author = models.CharField(max_length=200)
	affiliation = models.CharField(max_length=500)

	def __str__(self):
		return f"{self.title}"

