from django import forms


# Create your models here.
class SearchForm(forms.Form):
    location_field = forms.CharField(label='Location', max_length=100)
    zip_field = forms.IntegerField()