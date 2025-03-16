from random import choices
from django.core.validators import MaxValueValidator
from django.db import models
from inventory.models import *

# Create your models here.

class SalesOrder(models.Model):
    customer = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(validators=[MaxValueValidator(99999)], default=0)
    qty = models.IntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, default='Ctn', choices=[
        ('CTN', 'Ctn'),
        ('Pouch', 'Pouch')
    ])
    delivery = models.CharField(max_length=20, default='X.Mill', choices=[
        ('Xmill', 'X.Mill'),
        ('Pohonch', 'Pohonch')
    ])
    status = models.CharField(max_length=20, choices=[
        ('Draft', 'Draft'),
        ('SENT', 'Sent'),
        ('PAID', 'Paid'),
    ])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)  # Add ForeignKey to Inventory

