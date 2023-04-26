from django.contrib import admin
from django.urls import path
from gifs.views import gif_page, add_gif, add_category, increment_likes, decrement_likes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gif_page, name='homepage'),
    path('add_gif/', add_gif, name='add_gif'),
    path('add_category/', add_category, name='add_category'),
    path('gif/<int:gif_id>/increment_likes/', increment_likes, name='increment_likes'),
    path('gif/<int:gif_id>/decrement_likes/', decrement_likes, name='decrement_likes'),
]
