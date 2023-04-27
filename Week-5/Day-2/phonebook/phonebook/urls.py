from django.contrib import admin
from django.urls import path
from phone_app.views import search_person

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/<str:search_value>', search_person)
]
