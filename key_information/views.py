from django.shortcuts import render

# Create your views here.
from user.models import User


def key_info_index(request):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, "key_information/key_information.html", {
            'UserData': user.profilepicture,
        })
    else:
        return render(request, "key_information/key_information.html")