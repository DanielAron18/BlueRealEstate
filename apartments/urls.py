from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.get_apartment_by_id, name='apartment_details'),
]