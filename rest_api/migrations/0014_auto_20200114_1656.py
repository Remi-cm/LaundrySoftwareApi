# Generated by Django 3.0.2 on 2020-01-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0013_auto_20200113_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundry',
            name='imgUrl',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='time_expected',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='cni_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
