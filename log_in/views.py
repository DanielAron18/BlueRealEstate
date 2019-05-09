from django.shortcuts import render

# Create your views here.


def log_in_index(request):
    return render(request, "log_in/log_in.html")


def register_index(request):
    return render(request, "log_in/register.html")


def forgot_password_index(request):
    return render(request, "log_in/forgot_password.html")