from django.forms import widgets, ModelForm
from apartments.models import ApartmentImage

class AddApartmentImage(ModelForm):
    class Meta:
        model = ApartmentImage
        exclude = ['id', 'apartment']
        widgets = {
            'Image': widgets.Textarea(attrs={'class': 'form-control'}),
            'mainimage': widgets.CheckboxInput(attrs={'class': 'form-control'}),
        }