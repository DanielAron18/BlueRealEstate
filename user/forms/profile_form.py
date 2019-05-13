from django.forms import widgets, ModelForm
from user.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'user', 'username', 'password', 'searchhistory']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'socialsecurity': widgets.NumberInput(attrs={'class': 'form-control'}),
            'startdate': widgets.DateInput(attrs={'class': 'form-control'}),
            'cellphone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'profilepicture': widgets.TextInput(attrs={'class': 'form-control'}),
        }
