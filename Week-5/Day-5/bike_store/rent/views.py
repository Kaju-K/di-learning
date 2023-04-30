from django.shortcuts import render
from .models import Rental, Customer
from .forms import RentalForm, CustomerForm
from django.views import generic
from django.urls import reverse_lazy
from django_countries import countries

# Create your views here.
def rental_views(request):
    rentals = Rental.objects.order_by("-return_date", "rental_date")
    context = {"rentals":  rentals}
    return render(request, "rental_views.html", context)

def specific_rent(request, id):
    rent = Rental.objects.get(id=id)
    context = {'rent': rent}
    return render(request, "specific_rent.html", context)

class NewRental(generic.CreateView):
    template_name = 'new_rental.html'
    model = Rental
    form_class = RentalForm
    success_url = reverse_lazy('rental_views')

def specific_customer(request, id):
    customer = Customer.objects.get(id=id)
    customer_country = dict(countries)[customer.country]
    context = {"customer": customer, "customer_country": customer_country}
    return render(request, "specific_customer.html", context)

def customer_views(request):
    customers = Customer.objects.order_by("first_name", "last_name")
    context = {"customers": customers}
    return render(request, 'customer_views.html', context)

class NewCustomer(generic.CreateView):
    template_name = 'new_customer.html'
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer_views')