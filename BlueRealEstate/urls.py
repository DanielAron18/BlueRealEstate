"""BlueRealEstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apartments.views import order_by_price
from apartments.views import order_by_size
from apartments.views import zip_location_fields
from apartments.views import order, order_confirmation
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("index.urls")),
    #path('order_price/', include("index.urls")),
    path('key_information/', include("key_information.urls")),
    path('about_us/', include("about_us.urls")),
    path('contact_us/', include("contact_us.urls")),
    path('why_blue/', include("why_blue.urls")),
    path('location/', include("location.urls")),
    path('user/', include("user.urls")),
    path('apartment_details/', include("apartments.urls")),
    path('order_price/apartment_details/', include("apartments.urls")),
    path('order_size/apartment_details/', include("apartments.urls")),
    path('search/apartment_details/', include("apartments.urls")),
    path('order_price/', order_by_price, name='order_price'),
    path('order_size/', order_by_size, name='order_size'),
    path('search/', zip_location_fields, name='search'),
    path('order/', order, name='order'),
]
