from django.shortcuts import render

# Create your views here.
from user.models import User


def why_blue_index(request):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, "why_blue/why_blue.html", {
            'UserData': user.profilepicture,
        })
    else:
        return render(request, "why_blue/why_blue.html")