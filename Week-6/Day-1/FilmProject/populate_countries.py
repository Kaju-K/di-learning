import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FilmProject.settings')
django.setup()

from django_countries import countries
from films.models import Country

countries_dict = dict(countries)

for country in countries_dict.values():
    Country(name=country).save()   