from django.shortcuts import render, get_object_or_404
from apartments.models import Apartment
from django.contrib.postgres.search import SearchVector
from index.forms import SearchForm


# Create your views here.
def index(request):
    context = {'Apartments': Apartment.objects.all()}
    return render(request, 'apartments/single_apartment.html', context)


def get_apartment_by_id(request, id):
    return render(request, 'apartments/single_apartment_details.html', {
        'Apartment': get_object_or_404(Apartment, pk=id)
    })


def order_by_price(request):
    context = {'OrderByPrice': Apartment.objects.all().order_by('price')}
    return render(request, 'apartments/order_by_price.html', context)


def order_by_size(request):
    context = {'OrderBySize': Apartment.objects.all().order_by('size')}
    return render(request, 'apartments/order_by_size.html', context)


def zip_location_fields(request):
    zip_front = request.POST['zipfield']
    location = request.POST['locationfield'].lower()
    if zip_front != '' and location == '':
        context = {'ZipOrLocation': Apartment.objects.filter(postalcode=zip_front)}
        return render(request, 'apartments/search_zip.html', context)
    elif location != '' and zip_front == '':
        location = location.capitalize()
        context = {'ZipOrLocation': Apartment.objects.annotate(
            search=SearchVector('location', 'address', 'description')).filter(search=location)
        }
        return render(request, 'apartments/search_zip.html', context)
    else:
        return render(request, 'apartments/search_zip.html')

