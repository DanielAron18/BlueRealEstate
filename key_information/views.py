from django.shortcuts import render

# Create your views here.
from user.models import User


def key_info_index(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        return render(request, "key_information/key_information.html", {
            'UserData': user.profilepicture,
        })
    else:
        return render(request, "key_information/key_information.html")