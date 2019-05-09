from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile_index, name="user_profile"),

]