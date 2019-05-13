from django.shortcuts import render
from user.models import User
# Create your views here.
from apartments.models import Apartment


def index(request):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, "index/front_page.html", {
            'apartments': Apartment.objects.all(),
            'UserData': user.profilepicture,
        })
    else:
        return render(request, "index/front_page.html", {
            'apartments': Apartment.objects.all(),
        })
