from django.urls import path
from .views import (
    add_films,
    add_director,
    update_films
)

urlpatterns = [
    path('add_film/', add_films.as_view(), name="add_films"),
    path('add_director/', add_director.as_view(), name="add_director"),
    path('update_film/<int:pk>', update_films.as_view(), name="update_films"),
]