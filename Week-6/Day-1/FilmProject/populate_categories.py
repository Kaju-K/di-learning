import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FilmProject.settings')
django.setup()

from films.models import Category

categories = ["Action", "Terror", "Comedy", "Documentary", "Romance", "Suspense", "Drama", "Fantasy", "Horror", "Mistery", "Thriller", "Musical"]

for category in categories:
    Category(name=category).save()