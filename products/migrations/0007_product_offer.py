# Generated by Django 4.2.1 on 2023-08-09 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
        ('products', '0006_color_is_available_product_is_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='offer.offer'),
        ),
    ]
