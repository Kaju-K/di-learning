from django.contrib import admin
from django.urls import path
from rent.views import rental_views, specific_rent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/rental', rental_views, name="rental_views"),
    path('rent/rental/<int:id>', specific_rent, name="specific_rent"),
]
