# Generated by Django 4.2 on 2023-04-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gif',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
