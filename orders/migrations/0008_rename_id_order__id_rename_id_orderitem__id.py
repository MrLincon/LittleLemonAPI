# Generated by Django 5.0.6 on 2024-06-09 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='id',
            new_name='_id',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='id',
            new_name='_id',
        ),
    ]
