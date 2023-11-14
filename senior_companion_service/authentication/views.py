from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from .forms import UserRegistrationForm, UserProfileForm
from .models import User


class UserRegistrationView(View):
    """
    View for user registration.

    Attributes:
        template_name (str): HTML template for rendering the registration form.
        form_class: Form class for user registration.
    """

    template_name = "authentication/create_user.html"
    form_class = UserRegistrationForm

    def get(self, request, *args, **kwargs):
        """
        Handle GET request to render the registration form.

        Args:
            request: HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HTTP response with rendered registration form.
        """
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to process user registration.

        Args:
            request: HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HTTP response based on the success or failure of the registration.
        """
        form = self.form_class(request.POST)
        form_errors = None

        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data["password1"]
            user.save()
            return redirect("home")
        else:
            # Handling of form errors
            form_errors = form.errors
            for field, error_list in form_errors.items():
                for error in error_list:
                    messages.error(request, error)

        return redirect("home")


def login_view(request):
    """
    Handles user authentication.

    For POST requests, attempts to authenticate the user and redirects accordingly.
    For GET requests, displays the login form.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Redirects or renders the actual page.
    """
    if request.method == "POST":
        actual_page = request.POST.get("name_page", "home")

        # User authentication
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            messages.error(request, "User not found. Please verify your email.")
            return redirect(actual_page)

        authenticated_user = authenticate(request, email=email, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)

            if not remember_me:
                # If "Remember me" is not checked, set session expiration to 0 (logout when closing browser).
                request.session.set_expiry(0)

            messages.success(request, "Login successful!")
            return redirect(actual_page)
        else:
            messages.error(request, "Incorrect password. Please try again.")
            return redirect(actual_page)

    elif request.method == "GET":
        # Display the login form
        return render(request, "authentication/login_user.html")

    else:
        # Method not allowed
        messages.error(request, "Method not allowed")
        return redirect(actual_page)  # Redirect back to the actual page


@login_required
def logout_view(request):
    """
    Logs out the user and redirects to the home page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Redirects to the home page.
    """
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect("home")  # Redirect to the home page after logout


@login_required
def edit_user_profile(request):
    """
    View for editing a user's profile information.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is POST and the form is valid, the user's profile is updated,
        and a success message is displayed. If there are form errors, an error message is displayed.
        In both cases, the view redirects to the 'editGeneralAllCustomer' URL. If the request method is GET,
        the view renders a form populated with the user's current profile information.

    Note:
        This view assumes the existence of a UserProfileForm based on the User model.

    """
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
        else:
            messages.error(
                request,
                "Error updating profile. Please correct the errors in the form.",
            )
        return redirect("editGeneralAllCustomer")
    else:
        form = UserProfileForm(instance=request.user)

    return form
