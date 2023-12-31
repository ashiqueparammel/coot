# Generated by Django 4.2.4 on 2023-08-23 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_is_available'),
        ('banner', '0003_remove_banner_banner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
        migrations.AddField(
            model_name='banner',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
