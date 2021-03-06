# Generated by Django 3.0.2 on 2020-01-14 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0014_auto_20200114_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundry',
            name='agency',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='laundry',
            name='client',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='laundry',
            name='price_estimated',
            field=models.DecimalField(decimal_places=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='shipper',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='rest_api.Shipper'),
            preserve_default=False,
        ),
    ]
