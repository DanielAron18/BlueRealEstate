from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('log_in/', LoginView.as_view(template_name="user/log_in.html"), name="log_in"),
    path('log_out/', LogoutView.as_view(next_page='front_page'), name='log_out'),
    path('register/', views.register_index, name="register"),

    path('forgot_password/', views.forgot_password_index, name="forgot_password")
]
