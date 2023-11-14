from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.CustomerRegistrationView.as_view(), name="createCustomer"),
    path("edit/", views.edit_general_all_customer, name="editGeneralAllCustomer"),
    path(
        "edit/medicalInformation",
        views.editCreate_MedicalInformation,
        name="editMedicalInformation",
    ),
    path("edit/createPreference", views.create_preference, name="createPreference"),
    path(
        "edit/deletePreference/<int:idPreference>/",
        views.delete_preference,
        name="deletePreference",
    ),
    path("edit/userProfile", views.edit_user_profile, name="editUserProfile"),
    path("edit/customer", views.edit_customer, name="editCustomer"),
]
