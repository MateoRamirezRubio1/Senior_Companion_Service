from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    """
    Form for user registration, extending UserCreationForm.

    Attributes:
        user_type (ChoiceField): Field for selecting user type.

    Meta:
        model: User model.
        fields: List of fields to include in the form.
    """

    class Meta:
        model = User
        fields = ['names', 'lastNames', 'email', 'password1', 'password2']
