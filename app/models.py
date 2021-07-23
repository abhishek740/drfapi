from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import Collector

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Product(models.Model):
    product_name = models.CharField(max_length=1000)
    product_model_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name