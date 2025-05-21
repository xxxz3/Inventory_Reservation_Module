from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.name
