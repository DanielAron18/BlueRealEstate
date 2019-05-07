from django.shortcuts import render

# Create your views here.


def key_info_index(request):
    return render(request, "key_information/key_information.html")