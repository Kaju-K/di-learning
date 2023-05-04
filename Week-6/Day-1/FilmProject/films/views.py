from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Models
from .models import (
    Film,
    Director
)

# Forms
from .forms import (
    AddFilmForm,
    AddDirectorForm
)

class homepage(generic.ListView):
    template_name = "homepage.html"
    context_object_name = "films"
    model = Film


class add_films(generic.CreateView):
    template_name = "film/add_film.html"
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy("homepage")

class add_director(generic.CreateView):
    template_name = "director/add_director.html"
    model = Director
    form_class = AddDirectorForm
    success_url = reverse_lazy("homepage")

class update_films(generic.UpdateView):
    template_name = "film/update_film.html"
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy("homepage")

class update_director(generic.UpdateView):
    template_name = "director/update_director.html"
    model = Director
    form_class = AddDirectorForm
    success_url = reverse_lazy("homepage")
