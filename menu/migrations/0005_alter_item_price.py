# Generated by Django 5.0.6 on 2024-05-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]