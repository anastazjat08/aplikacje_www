from django.db import models
import datetime
from django.utils import timezone

# Create your models here.



class Comment(models.Model):
	text = models.CharField(max_length=500)
	author = models.CharField(max_length=100)
	date_creation = models.DateTimeField()
	date_published = models.DateTimeField()

