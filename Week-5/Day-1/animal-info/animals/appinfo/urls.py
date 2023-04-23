from django.urls import path
from . import views

urlpatterns = [
    path('family/2', views.caninae),
    path('family/1', views.felidae),
    path('animal/1', views.dog),
    path('animal/2', views.domestic_cat),
    path('animal/3', views.panther)
]