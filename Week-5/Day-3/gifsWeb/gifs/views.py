from django.shortcuts import render, redirect
from .models import Gif, Category
from .forms import GifForm, CategoryForm
from django.http import HttpResponse
# Create your views here.

def add_gif(request):

    gif_form = GifForm()

    if request.method == "POST":
        gif_filled_form = GifForm(request.POST)
        if gif_filled_form.is_valid():
            gif_filled_form.save()
            
            context = {'message': "Gif"}

            return render(request, 'successfull.html', context)
    context = {'form': gif_form}

    return render(request, 'add_gif.html', context)


def add_category(request):
    category_form = CategoryForm()
    if request.method == "POST":
        category_filled_form = CategoryForm(request.POST)
        if category_filled_form.is_valid():
            category_filled_form.save()
            context = {'message': "category"}
            return render(request, 'successfull.html', context)
    context = {'form': category_form}
    return render(request, 'add_category.html', context)
    
def increment_likes(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    gif.likes += 1
    gif.save()
    return redirect('homepage')

def decrement_likes(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    gif.likes -= 1
    gif.save()
    return redirect('homepage')

def gif_page(request):
    selected_categories = request.GET.getlist('category')
    int_selected_categories = list(map(lambda x: int(x), selected_categories))
    gifs = Gif.objects.all().order_by('title')
    if selected_categories:
        categories = Category.objects.filter(id__in=selected_categories)
        gifs = list(set(gifs.filter(categories__in=categories)))
    context = {'gifs': gifs, 'categories': Category.objects.all(), 'selected_categories': int_selected_categories}
    return render(request, 'gif_page.html', context)