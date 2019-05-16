from django.shortcuts import render

# Create your views here.
from user.models import User


def why_blue_index(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.id)
        return render(request, "why_blue/why_blue.html", {
            'UserData': user.profilepicture,
        })
    else:
        return render(request, "why_blue/why_blue.html")