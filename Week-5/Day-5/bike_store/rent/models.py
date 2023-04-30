from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(unique=True, null=False)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = CountryField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class VehicleType(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return f"{self.name}"

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.PROTECT)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.FloatField()
    size = models.ForeignKey("VehicleSize", on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.vehicle_type}"

class VehicleSize(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Rental(models.Model):
    rental_date = models.DateField(default = timezone.now)
    return_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey("Customer", on_delete=models.PROTECT)
    vehicle = models.ForeignKey("Vehicle", on_delete=models.PROTECT)

    def __str__(self) -> str:
        if self.return_date:
            return f"{self.customer} rented a {self.vehicle} on {self.rental_date} and returned on {self.return_date}"
        return f"{self.customer} rented a {self.vehicle} on {self.rental_date} and still didn't returned"

class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.PROTECT)
    vehicle_size = models.ForeignKey("VehicleSize", on_delete=models.PROTECT)
