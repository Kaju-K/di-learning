# Generated by Django 4.2 on 2023-04-29 20:23

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('real_cost', models.FloatField()),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.vehiclesize')),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='RentalRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_rate', models.IntegerField()),
                ('vehicle_size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.vehiclesize')),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField()),
                ('return_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.vehicle')),
            ],
        ),
    ]
