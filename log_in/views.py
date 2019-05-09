from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


def log_in_index(request):
    return render(request, "log_in/log_in.html")


def register_index(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request, "log_in/register.html", {
        'form': UserCreationForm(data=request.POST)
    })


def forgot_password_index(request):
    return render(request, "log_in/forgot_password.html")