from django.forms import widgets, ModelForm
from user.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'socialsecurity': widgets.TextInput(attrs={'class': 'form-control'}),
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
            'startdate': widgets.TextInput(attrs={'class': 'form-control'}),
            'profilepicture': widgets.TextInput(attrs={'class': 'form-control'}),
            'cellphone': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'searchhistory': widgets.TextInput(attrs={'class': 'form-control'}),
        }
