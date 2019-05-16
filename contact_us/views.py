from django.shortcuts import render, redirect


# Create your views here.
from contact_us.forms.new_message import ContactUsForm
from contact_us.models import Messages
from user.models import User


def contact_us_index(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(user_id=request.user.id)
        except:
            user = None
        if user != None:
            form = ContactUsForm(data=request.POST)
            if form.is_valid():
                message = Messages()
                message.name = request.POST['name']
                message.phonenumber = request.POST['phonenumber']
                message.email = request.POST['email']
                message.message = request.POST['message']
                message.save()
                return redirect('front_page')
        else:
            form = ContactUsForm(data=request.POST)
            if form.is_valid():
                message = Messages()
                message.name = request.POST['name']
                message.phonenumber = request.POST['phonenumber']
                message.email = request.POST['email']
                message.message = request.POST['message']
                message.save()
                return redirect('front_page')
    else:
        try:
            user = User.objects.get(user_id=request.user.id)
        except:
            user = None
        if user != None:
            return render(request, "contact_us/contact_us.html", {
                'UserData': user.profilepicture,
                'form': ContactUsForm
            })
        else:
            return render(request, "contact_us/contact_us.html", {
                'form': ContactUsForm
            })
