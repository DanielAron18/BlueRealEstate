from django.forms import widgets, ModelForm

from apartments.models import Apartment
from user.models import User


class AddApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id', 'agentid']
        widgets = {
            'postalcode': widgets.TextInput(attrs={'class': 'form-control'}),
            'location': widgets.NumberInput(attrs={'class': 'form-control'}),
            'adress': widgets.DateInput(attrs={'class': 'form-control'}),
            'bedrooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'size': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
        }