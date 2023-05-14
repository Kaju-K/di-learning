from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Country(models.Model):
    name = CountryField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    created_in_country = models.ForeignKey("Country", on_delete=models.PROTECT)
    available_in_countries = models.ManyToManyField("Country", related_name="films")
    category = models.ManyToManyField("Category", related_name='films')
    director = models.ManyToManyField("Director", related_name='films')

    def __str__(self) -> str:
        return f"{self.title}"

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Comments(models.Model):
    comment = models.CharField(max_length=200)
    film = models.ForeignKey("Film", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.comment