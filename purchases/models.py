from django.db import models

# Create your models here.
class PurchaseOrder(models.Model):
    supplier = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('RECEIVED', 'Received'),
        ('COMPLETED', 'Completed'),
    ])