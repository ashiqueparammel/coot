# Generated by Django 4.2.1 on 2023-07-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='single_total',
            field=models.BigIntegerField(default=0),
        ),
    ]
