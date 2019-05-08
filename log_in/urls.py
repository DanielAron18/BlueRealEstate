from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in_index, name="log_in"),
]
