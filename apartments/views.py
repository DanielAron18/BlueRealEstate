from django.shortcuts import render, get_object_or_404, redirect

from apartments.forms.add_apartment import AddApartmentForm
from apartments.forms.apartment_order import ApartmentOrderForm
from apartments.models import Apartment, ApartmentOrder
from django.contrib.postgres.search import SearchVector
from index.forms import SearchForm
from index.models import Search


# Create your views here.
from user.models import User


def index(request):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, 'apartments/single_apartment.html', {
            'Apartments': Apartment.objects.all(),
            'UserData': user.profilepicture
        })
    else:
        return render(request, 'apartments/single_apartment.html', {
            'Apartments': Apartment.objects.all()
        })


def get_apartment_by_id(request, id):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
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
        return render(request, 'apartments/order_by_price.html', {
            'OrderByPrice': Apartment.objects.all().order_by('price')
        })


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
        return render(request, 'apartments/order_by_size.html', {
            'OrderBySize': Apartment.objects.all().order_by('size')
        })


def zip_location_fields(request):

    zip_front = request.POST['zipfield']
    location = request.POST['locationfield'].lower()

    if location is not None and zip_front is '':
        Search.objects.create(location=location, zip='None')
    elif zip_front is not None and location is '':
        Search.objects.create(location='None', zip=zip_front)

    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
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


def search_and_arrange_price(request):
    latest_id = Search.objects.latest('id')
    if latest_id.location == 'None' and latest_id.zip:
        context = {'SearchArrange': Apartment.objects.filter(postalcode=latest_id.zip).order_by('price')}
    else:
        context = {'SearchArrange': Apartment.objects.annotate(
                search=SearchVector('location', 'address', 'description')).filter(search=latest_id.location).order_by('price')}
    return render(request, 'apartments/search_arrange.html', context)


def search_and_arrange_size(request):
    latest_id = Search.objects.latest('id')
    if latest_id.location == 'None' and latest_id.zip:
        context = {'SearchArrange': Apartment.objects.filter(postalcode=latest_id.zip).order_by('size')}
    else:
        context = {'SearchArrange': Apartment.objects.annotate(
                search=SearchVector('location', 'address', 'description')).filter(search=latest_id.location).order_by('size')}
    return render(request, 'apartments/search_arrange.html', context)


def add_apartment(request):
    if request.method == 'POST':
        new_apartments = Apartment
        form = AddApartmentForm(data=request.POST)
        if form.is_valid():
            new_apartments.price = request.POST['price']
            new_apartments.location = request.POST['location']
            new_apartments.address = request.POST['address']
            new_apartments.bedrooms = request.POST['bedrooms']
            new_apartments.description = request.POST['description']
            new_apartments.postalcode = request.POST['postalcode']
            new_apartments.size = request.POST['size']
            new_apartments.agentid = request.user.id
            new_apartments.save()
            return redirect('profile')
    else:
        return render(request, 'apartments/add_apartment.html', {
            'form': AddApartmentForm()
        })


def order(request, id):
    if request.method == 'POST':
        try:
            user = User.objects.get(user_id=request.user.id)
        except:
            user = None
        if user != None:
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
                print('YOU CAN NOT BE HERE')
    else:
        try:
            user = User.objects.get(user_id=request.user.id)
        except:
            user = None
        if user != None:
            return render(request, 'apartments/order.html', {
                'Apartment': get_object_or_404(Apartment, pk=id),
                'UserData': user.profilepicture,
                'form': ApartmentOrderForm
            })
        else:
            return redirect('register')


def order_confirmation(request, id):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, 'apartments/order_confirmation.html', {
            'Apartment': get_object_or_404(Apartment, pk=id),
            'UserData': user.profilepicture})

    else:
        return render(request, 'apartments/order_confirmation.html', {
            'Apartment': get_object_or_404(Apartment, pk=id)
        })


def order_success(request, id):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, 'apartments/order_success.html', {
            'Apartment': get_object_or_404(Apartment, pk=id),
            'UserData': user.profilepicture})
    else:
        return render(request, 'apartments/order_success.html', {
            'Apartment': get_object_or_404(Apartment, pk=id)
        })