from django.shortcuts import render, redirect

from contact_us.forms import ContactUsForm

# Create your views here.
from contact_us.models import Messages
from user.models import User


def contact_us_index(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = User.objects.get(user_id=request.user.id)
            form = ContactUsForm(data=request.POST)
            if form.is_valid():
                message = Messages()
                message.name = request.POST['name']
                message.phonenumber = request.POST['phone']
                message.email = request.POST['email']
                message.message = request.POST['message']
                message.save()
                return redirect('front_page')
        else:
            form = ContactUsForm(data=request.POST)
            if form.is_valid():
                message = Messages()
                message.name = request.POST['name']
                message.phonenumber = request.POST['phone']
                message.email = request.POST['email']
                message.message = request.POST['message']
                message.save()
                return redirect('front_page')
    else:
        if request.user.is_authenticated:
            user = User.objects.get(user_id=request.user.id)
            return render(request, "contact_us/contact_us.html", {
                'UserData': user.profilepicture,
                'form': ContactUsForm
            })
        else:
            return render(request, "contact_us/contact_us.html", {
                'form': ContactUsForm
            })
