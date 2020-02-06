# Generated by Django 3.0.2 on 2020-01-16 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0018_auto_20200114_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothe',
            name='colour',
        ),
        migrations.RemoveField(
            model_name='clothe',
            name='description',
        ),
        migrations.RemoveField(
            model_name='clothe',
            name='laundry',
        ),
        migrations.AlterField(
            model_name='laundry',
            name='price_estimated',
            field=models.DecimalField(decimal_places=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=0, max_digits=9),
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='No description', max_length=255)),
                ('price', models.DecimalField(decimal_places=0, max_digits=6)),
                ('color', models.CharField(default='Not specified', max_length=20)),
                ('clothe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.Clothe')),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.Laundry')),
            ],
        ),
    ]
