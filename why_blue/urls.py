from django.urls import path
from . import views

urlpatterns = [
    path('', views.why_blue_index, name="why_blue"),
]