from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homeReserve, name='homeReserve'),
    path('booking/',views.booking, name='booking'),
    path('bookingSubmit/',views.bookingSubmit, name='bookingSubmit'),

]