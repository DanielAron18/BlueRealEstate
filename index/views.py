from django.shortcuts import render

# Create your views here.

from apartments.models import Apartment

def index(request):
    context = {'apartments': Apartment.objects.all() }
    return render(request, "index/front_page.html", context)
