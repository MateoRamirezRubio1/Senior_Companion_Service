from django.http import Http404
from django.db import IntegrityError, transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from authentication.views import UserRegistrationView
from authentication.models import User
from .models import Customer

class CustomerRegistrationView(UserRegistrationView):
    """
    View for customer registration, extending UserRegistrationView.

    Attributes:
        None.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to process customer registration.

        Args:
            request: HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HTTP response based on the success or failure of the registration.
        """
        response = redirect('home')

        try:
            with transaction.atomic():
                response = super().post(request, *args, **kwargs)
                user = get_object_or_404(User, email=request.POST['email'])
                customer = Customer.objects.create(idUser=user, accountState='activo')
                return redirect('home')

        except IntegrityError:
            messages.error(request, 'Error: A Customer with this email already exists.')
            return redirect('home')
        
        except Http404:
            return response
