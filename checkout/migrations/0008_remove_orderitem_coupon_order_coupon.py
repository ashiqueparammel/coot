# Generated by Django 4.2.1 on 2023-08-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_orderitem_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='coupon',
        ),
    
    ]
