from django.db import models

# Create your models here.
class Product(models.Model):
	""""docstring for product"""
	title = models.CharField(max_length = 120)
	description = models.TextField(blank =  True, null = True)
	price = models.DecimalField(decimal_places = 2, max_digits = 10000)
	summary = models.TextField(default = 'this is so cool!')
	featured = models.BooleanField(default=True)
