from django.urls import path
from .views import (
    add_films,
    add_director,
    update_films,
    delete_movie,
    film_page,
    add_comment,
)

urlpatterns = [
    path('add_film/', add_films.as_view(), name="add_films"),
    path('add_director/', add_director.as_view(), name="add_director"),
    path('update_film/<int:pk>', update_films.as_view(), name="update_films"),
    path('delete_movie/<int:id>', delete_movie, name="delete_movie"),
    path('add_comment/', add_comment, name="add_comment"),
    path('<int:id>', film_page, name='film_page')
]