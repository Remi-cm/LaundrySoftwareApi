# Generated by Django 3.0.2 on 2020-01-31 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0025_auto_20200128_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothe',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='onDelivery',
            field=models.CharField(default='No', max_length=5),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='phone',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
