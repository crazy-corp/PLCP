from django.db import models

# Create your models here.
class plcp(models.Model):
	dt = models.DateTimeField()
	Voltage = models.IntegerField()
	Current = models.IntegerField()
	Power = models.IntegerField()
	pf = models.DecimalField(max_digits=3,decimal_places=2,default=1.00)
	