# Generated by Django 5.0.6 on 2024-05-20 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='item',
            new_name='item_id',
        ),
    ]