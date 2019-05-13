from django.shortcuts import render, get_object_or_404
from apartments.models import Apartment


# Create your views here.
def index(request):
    context = {'Apartments': Apartment.objects.all()}
    return render(request, 'apartments/single_apartment.html', context)


def get_apartment_by_id(request, id):
    return render(request, 'apartments/single_apartment_details.html', {
        'Apartment': get_object_or_404(Apartment, pk=id)
    })