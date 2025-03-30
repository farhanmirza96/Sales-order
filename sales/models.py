from random import choices
from typing import override
from django.core.validators import MaxValueValidator
from django.db import models
from inventory.models import *

# Create your models here.

class SalesOrder(models.Model):
    customer = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(validators=[MaxValueValidator(99999)], default=0)
    qty = models.IntegerField(default=1)
    remaining_qty = models.IntegerField(default=0)
    invoiced_qty = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, default='Ctn', choices=[
        ('CTN', 'Ctn'),
        ('Pouch', 'Pouch')
    ])
    delivery = models.CharField(max_length=20, default='X.Mill', choices=[
        ('Xmill', 'X.Mill'),
        ('Pohonch', 'Pohonch')
    ])
    status = models.CharField(max_length=20, default='Pending', choices=[
        ('In process', 'In process'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)  # Add ForeignKey to Inventory

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=150)

    @override
    def __str__(self):
        return self.first_name + '   ' + self.last_name

class Invoice(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    invoice_date = models.DateTimeField(auto_now_add=True)
    invoice_number = models.CharField(max_length=20)
    invoice_qty = models.IntegerField(default=1)
    invoice_rate = models.IntegerField(validators=[MaxValueValidator(99999)], default=0)
    invoice_total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    @override
    def __str__(self):
        return f'Invoice {self.invoice_number} for Order {self.sales_order.id} - Amount: {self.invoice_total_amount}'
