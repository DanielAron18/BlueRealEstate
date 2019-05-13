from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us_index, name="about_us"),
]