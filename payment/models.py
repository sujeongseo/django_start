from django.db import models

# Create your models here.

class Order(models.Model):
    product_name = models.TextField()
    price = models.TextField()
    payment_method = models.TextField()
    ordered_at = models.DateTimeField(auto_now_add=True)
