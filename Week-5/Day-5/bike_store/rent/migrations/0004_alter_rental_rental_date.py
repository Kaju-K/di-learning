# Generated by Django 4.2 on 2023-04-30 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_alter_rental_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 30, 11, 23, 4, 290701)),
        ),
    ]
