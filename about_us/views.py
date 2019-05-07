from django.shortcuts import render

# Create your views here.


def key_info_index(request):
    return render(request, "about_us/about_us.html")