from django.shortcuts import render
from django.views.generic import TemplateView

from contact_us.forms import ContactUsForm

# Create your views here.
from user.models import User


def contact_us_index(request):
    try:
        user = User.objects.get(user_id=request.user.id)
    except:
        user = None
    if user != None:
        return render(request, "contact_us/contact_us.html", {
            'UserData': user.profilepicture,
        })
    else:
        return render(request, "contact_us/contact_us.html")
