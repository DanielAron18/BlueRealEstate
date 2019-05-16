from django.forms import ModelForm, widgets

from contact_us.models import Messages


class ContactUsForm(ModelForm):
    class Meta:
        model = Messages
        exclude = ['id']
        widgets = {
            'name': widgets.Textarea(attrs={'class': 'form-control'}),
            'email': widgets.Textarea(attrs={'class': 'form-control'}),
            'phonenumber': widgets.Textarea(attrs={'class': 'form-control'}),
            'message': widgets.Textarea(attrs={'class': 'form-control'}),
        }