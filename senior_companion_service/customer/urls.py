from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CustomerRegistrationView.as_view(), name='createCustomer'),
]