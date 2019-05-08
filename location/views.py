from django.shortcuts import render

# Create your views here.


def location_index(request):
    return render(request, "location/location.html")