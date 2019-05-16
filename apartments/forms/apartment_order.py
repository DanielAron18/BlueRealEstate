from django.forms import widgets, ModelForm
from apartments.models import ApartmentOrder


class AddApartmentForm(ModelForm):
    class Meta:
        model = ApartmentOrder
        exclude = ['id', 'user']
        widgets = {
            'cardholdername': widgets.TextInput(attrs={'class': 'form-control'}),
            'cardnumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'exp': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvv': widgets.NumberInput(attrs={'class': 'form-control'}),
        }