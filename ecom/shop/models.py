from django.db import models

# Create your models here.
class Product (models.Model):

      product_name=models.CharField(max_length=30)
      product_desc=models.CharField(max_length=300)
      pub_date=models.DateField()