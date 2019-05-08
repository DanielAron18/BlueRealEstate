from django.shortcuts import render
from django.views.generic import TemplateView

from contact_us.forms import ContactUsForm

# Create your views here.



def contact_us_index(request):
    return render(request, "contact_us/contact_us.html")

def post(request):
    form = ContactUsForm(request.POST)

    if form.is_valid():
        name = form.cleaned_data['name']
