from django import forms
from .models import Rental, Customer


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ("customer", "vehicle")
        widgets = {
            'customer': forms.Select(attrs={'class': 'select'}),
            'vehicle': forms.Select(attrs={'class': 'select'})
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'