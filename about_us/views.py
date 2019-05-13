from django.shortcuts import render
# Create your views here.
from user.models import User


def about_us_index(request):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, "about_us/about_us.html", {
            'UserData': user.profilepicture,
        })
    else:
        return render(request, "about_us/about_us.html")
