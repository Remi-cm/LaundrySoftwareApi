# Generated by Django 3.0.2 on 2020-01-31 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0027_auto_20200131_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundry',
            name='onDelivery',
            field=models.BooleanField(default=False),
        ),
    ]
