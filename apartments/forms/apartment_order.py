from django.forms import widgets, ModelForm
from apartments.models import ApartmentOrder

from django_countries.data import COUNTRIES


class ApartmentOrderForm(ModelForm):
    class Meta:
        model = ApartmentOrder
        exclude = ['id', 'user']
        widgets = {
            'streetname': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Name'}),
            'housenumber': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'House Number'}),
            'city': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'country': widgets.Select(choices=sorted(COUNTRIES.items()), attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'postalcode': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'PostalCode'}),
            'ssn': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Social Security Number'}),
            'cardholdername': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cardholder Name'}),
            'cardnumber': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Number'}),
            'exp': widgets.DateInput(attrs={'class': 'form-control', 'placeholder': 'Exp Date'}),
            'cvv': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cvv'}),
        }