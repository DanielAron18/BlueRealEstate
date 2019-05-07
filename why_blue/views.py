from django.shortcuts import render

# Create your views here.


def why_blue_index(request):
    return render(request, "why_blue/why_blue.html")