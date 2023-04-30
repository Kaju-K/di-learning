from django.contrib import admin
from django.urls import path
from rent.views import rental_views, specific_rent, NewRental, specific_customer, customer_views, NewCustomer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/rental', rental_views, name="rental_views"),
    path('rent/rental/<int:id>', specific_rent, name="specific_rent"),
    path('rent/rental/add', NewRental.as_view(), name="new_rental"),
    path('rent/customer/<int:id>', specific_customer, name="specific_customer"),
    path('rent/customer', customer_views, name="customer_views"),
    path('rent/customer/add', NewCustomer.as_view(), name="new_customer")
]
