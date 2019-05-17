from django.forms import widgets, ModelForm
from apartments.models import Apartment

class AddApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id', 'agentid']
        widgets = {
            'postalcode': widgets.TextInput(attrs={'class': 'form-control'}),
            'location': widgets.TextInput(attrs={'class': 'form-control'}),
            'adress': widgets.TextInput(attrs={'class': 'form-control'}),
            'bedrooms': widgets.TextInput(attrs={'class': 'form-control'}),
            'size': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
        }