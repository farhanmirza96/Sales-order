# Generated by Django 5.1.7 on 2025-03-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0013_invoice_invoice_unit_invoice_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='status',
            field=models.CharField(choices=[('In process', 'In process'), ('Pending', 'Pending'), ('Hold', 'Hold'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
