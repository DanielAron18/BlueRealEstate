from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms.profile_form import UserForm
from user.models import User

# Create your views here.


def log_in_index(request):
    return render(request, "user/log_in.html")


def profile_index(request):
    user = User.objects.get(user_id=request.user.id)
    return render(request, "user/user_profile.html", {
        'userData': user
    })


def edit_profile_index(request):
    profile = User.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = UserForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.username = request.user.username
            profile.password = request.user.password
            profile.save()
            return redirect("profile")
    else:
        return render(request, 'user/edit_profile.html', {
            'form': UserForm(instance=profile)
        })


def register_index(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request, "user/register.html", {
        'form': UserCreationForm(data=request.POST)
    })


def forgot_password_index(request):
    return render(request, "index/front_page.html")
