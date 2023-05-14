from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Models
from .models import (
    Film,
    Director,
    Comments
)

# Forms
from .forms import (
    AddFilmForm,
    AddDirectorForm,
    CommentsForm
)

# class homepage(generic.ListView):
#     template_name = "homepage.html"
#     context_object_name = "films"
#     model = Film

def homepage(request):
    context = {}
    films = Film.objects.all().order_by("release_date")
    context["films"] = films
    return render(request, "homepage.html", context)

def delete_movie(request, id):
    film = get_object_or_404(Film, id=id)
    if request.user.is_superuser:
        film.delete()
        messages.success(request, f"{film.title} deleted successfully")
    elif request.user.is_authenticated:
        messages.error(request, "You are not allowed to delete films.")
    else:
        return redirect("login")
    return redirect("homepage")

@login_required(login_url='homepage')
def film_page(request, id):
    film = get_object_or_404(Film, id=id)
    comments = Comments.objects.filter(film=film.id)
    form = CommentsForm(initial={
        "film": film,
        "user": request.user
    })
    context = {
        "film": film,
        "comments": comments,
        "form": form,
    }
    return render(request, 'film/film_page.html', context)

def add_comment(request):
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_page', id=dict(request.POST)['film'][0])

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
