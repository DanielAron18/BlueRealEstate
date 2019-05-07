from django.urls import path
from . import views

urlpatterns = [
    path('', views.key_info_index, name="key_info"),
]
