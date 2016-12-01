from django.db import models

class Product(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=50)
	price=models.FloatField(null=True, blank=True, default=0)
	rating=models.FloatField(null=True, blank=True, default=0)
	description=models.TextField()
	genre=models.CharField(max_length=10)

	def __str__(self):
		return self.name
