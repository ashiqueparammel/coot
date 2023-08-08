# Generated by Django 4.2.1 on 2023-08-08 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='size',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]