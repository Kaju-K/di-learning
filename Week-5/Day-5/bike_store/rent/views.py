from django.shortcuts import render
from .models import Rental

# Create your views here.
def rental_views(request):
    rentals = Rental.objects.order_by("-return_date", "rental_date")
    context = {"rentals":  rentals}
    return render(request, "rental_views.html", context)

def specific_rent(request, id):
    rent = Rental.objects.get(id=id)
    context = {'rent': rent}
    return render(request, "specific_rent.html", context)