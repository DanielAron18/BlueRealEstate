from django.shortcuts import render

# Create your views here.
from user.models import User


def location_index(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        return render(request, 'location/location.html', {
            'UserData': user.profilepicture,
        })
    else:
        return render(request, "location/location.html")
