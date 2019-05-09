from django.shortcuts import render

# Create your views here.
def user_profile_index(request):
    return render(request, 'user_profile/user_profile.html')