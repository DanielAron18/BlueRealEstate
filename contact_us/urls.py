from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us_index, name="contact_us"),
]