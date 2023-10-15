from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CompanionRegistrationView.as_view(), name='createCompanion'),
]