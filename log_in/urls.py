from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in_index, name="log_in"),

    path('register/', views.register_index, name="register"),

    path('forgot_password/', views.forgot_password_index, name="forgot_password")
]
