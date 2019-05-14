from django.shortcuts import render, get_object_or_404, redirect

from apartments.forms.add_apartment import AddApartmentForm
from apartments.models import Apartment


# Create your views here.
def index(request):
    context = {'Apartments': Apartment.objects.all()}
    return render(request, 'apartments/single_apartment.html', context)


def get_apartment_by_id(request, id):
    return render(request, 'apartments/single_apartment_details.html', {
        'Apartment': get_object_or_404(Apartment, pk=id)
    })


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
