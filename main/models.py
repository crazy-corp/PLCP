from django.db import models

# Create your models here.
class plcp(models.Model):
	dt = models.DateTimeField()
	Voltage = models.IntegerField()
	Current = models.IntegerField()
	Power = models.IntegerField()
	