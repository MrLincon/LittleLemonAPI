# Generated by Django 5.0.6 on 2024-06-06 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_category_item_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category_id',
            field=models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='menu.category'),
        ),
    ]