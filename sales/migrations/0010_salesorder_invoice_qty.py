# Generated by Django 5.1.7 on 2025-03-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_salesorder_remaining_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='invoice_qty',
            field=models.IntegerField(default=0),
        ),
    ]
