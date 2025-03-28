# Generated by Django 5.1.6 on 2025-03-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_salesorder_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
    ]
