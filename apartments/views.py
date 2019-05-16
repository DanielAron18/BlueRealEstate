from django.db.models import Func, F, Value
from django.shortcuts import render, get_object_or_404, redirect

from apartments.forms.add_apartment import AddApartmentForm
from apartments.models import Apartment
from django.contrib.postgres.search import SearchVector
from index.forms import SearchForm


# Create your views here.
from user.models import User


def index(request):
    context = {'Apartments': Apartment.objects.all()}
    return render(request, 'apartments/single_apartment.html', context)


def get_apartment_by_id(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        if user.searchhistory:
            user.searchhistory.append(id)
            user.save()
        else:
            user.searchhistory = [id]
            user.save()
    return render(request, 'apartments/single_apartment_details.html', {
        'Apartment': get_object_or_404(Apartment, pk=id)
    })

def order_by_price(request):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, "apartments/order_by_price.html", {
            'OrderByPrice': Apartment.objects.all().order_by('price'),
            'UserData': user.profilepicture,
        })
    else:
        context = {'OrderByPrice': Apartment.objects.all().order_by('price')}
        return render(request, 'apartments/order_by_price.html', context)


def order_by_size(request):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, 'apartments/order_by_size.html', {
            'OrderBySize': Apartment.objects.all().order_by('size'),
            'UserData': user.profilepicture,
        })
    else:
        context = {'OrderBySize': Apartment.objects.all().order_by('size')}
        return render(request, 'apartments/order_by_size.html', context)


def zip_location_fields(request):
    zip_front = request.POST['zipfield']
    location = request.POST['locationfield'].lower()
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        zip_front = request.POST['zipfield']
        location = request.POST['locationfield'].lower()
        if zip_front != '' and location == '':
            context = {'ZipOrLocation': Apartment.objects.filter(postalcode=zip_front),
                       'UserData': user.profilepicture}
            return render(request, 'apartments/search_zip.html', context)
        elif location != '' and zip_front == '':
            location = location.capitalize()
            context = {'ZipOrLocation': Apartment.objects.annotate(
                search=SearchVector('location', 'address', 'description')).filter(search=location),
                       'UserData': user.profilepicture
            }
            return render(request, 'apartments/search_zip.html', context)
        else:
            return render(request, 'apartments/search_zip.html')
    else:
        if zip_front != '' and location == '':
            context = {'ZipOrLocation': Apartment.objects.filter(postalcode=zip_front)}
            return render(request, 'apartments/search_zip.html', context)
        elif location != '' and zip_front == '':
            location = location.capitalize()
            context = {'ZipOrLocation': Apartment.objects.annotate(
                search=SearchVector('location', 'address', 'description')).filter(search=location)}
            return render(request, 'apartments/search_zip.html', context)
        else:
            return render(request, 'apartments/search_zip.html')

def add_apartment(request):
    profile = Apartment.objects.filter().first()
    if request.method == 'post':
        form = AddApartmentForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.agentid = request.user.id
            profile.save()
            return redirect('profile')
    else:
        return render(request, 'apartments/add_apartment.html', {
            'form': AddApartmentForm(instance=profile)
        })


def order(request, id):
    return render(request, 'apartments/order.html', {
        'Apartment': get_object_or_404(Apartment, pk=id)
    })


def order_confirmation(request, id):
    return render(request, 'apartments/order_confirmation.html', {
        'Apartment': get_object_or_404(Apartment, pk=id)
    })