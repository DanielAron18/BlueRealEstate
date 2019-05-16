from django.shortcuts import render, get_object_or_404, redirect

from apartments.forms.add_apartment import AddApartmentForm
from apartments.forms.apartment_order import ApartmentOrderForm
from apartments.models import Apartment, ApartmentOrder
from django.contrib.postgres.search import SearchVector


# Create your views here.
from user.models import User


def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        return render(request, 'apartments/single_apartment.html', {
            'Apartments': Apartment.objects.all(),
            'UserData': user.profilepicture
        })
    else:
        return render(request, 'apartments/single_apartment.html', {
            'Apartments': Apartment.objects.all()
        })


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
            'Apartment': get_object_or_404(Apartment, pk=id),
            'UserData': user.profilepicture
        })
    else:
        return render(request, 'apartments/single_apartment_details.html', {
            'Apartment': get_object_or_404(Apartment, pk=id)
        })


def order_by_price(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        return render(request, "apartments/order_by_price.html", {
            'OrderByPrice': Apartment.objects.all().order_by('price'),
            'UserData': user.profilepicture,
        })
    else:
        return render(request, 'apartments/order_by_price.html', {
            'OrderByPrice': Apartment.objects.all().order_by('price')
        })


def order_by_size(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        return render(request, 'apartments/order_by_size.html', {
            'OrderBySize': Apartment.objects.all().order_by('size'),
            'UserData': user.profilepicture,
        })
    else:
        return render(request, 'apartments/order_by_size.html', {
            'OrderBySize': Apartment.objects.all().order_by('size')
        })


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
    if request.method == 'POST':
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
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = User.objects.get(user_id=request.user.id)
            form = ApartmentOrderForm(data=request.POST)
            if form.is_valid():
                order = ApartmentOrder()
                order.user = request.user
                order.cardholdername = request.POST['cardholdername']
                order.cardnumber = request.POST['cardnumber']
                order.exp = request.POST['exp']
                order.cvv = request.POST['cvv']
                order.save()
                return render(request, 'apartments/order_confirmation.html', {
                    'Apartment': get_object_or_404(Apartment, pk=id),
                    'UserData': user.profilepicture,
                    'OrderInfo': order
                })
            else:
                print('something more to come')
    else:
        if request.user.is_authenticated:
            user = User.objects.get(user_id=request.user.id)
            return render(request, 'apartments/order.html', {
                'Apartment': get_object_or_404(Apartment, pk=id),
                'UserData': user.profilepicture,
                'form': ApartmentOrderForm
            })
        else:
            return redirect('register')


def order_confirmation(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        return render(request, 'apartments/order_confirmation.html', {
            'Apartment': get_object_or_404(Apartment, pk=id),
            'UserData': user.profilepicture})
    else:
        return render(request, 'apartments/order_confirmation.html', {
            'Apartment': get_object_or_404(Apartment, pk=id)
        })