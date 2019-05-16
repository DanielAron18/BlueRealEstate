from django.shortcuts import render
from user.models import User
# Create your views here.
from apartments.models import Apartment


def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        return render(request, "index/front_page.html", {
            'apartments': Apartment.objects.all(),
            'UserData': user.profilepicture,
        })
    else:
        return render(request, "index/front_page.html", {
            'apartments': Apartment.objects.all(),
        })
