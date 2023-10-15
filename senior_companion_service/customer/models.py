from django.db import models
from authentication.models import User

class Customer(models.Model):
    """
    Model for representing a customer.

    Attributes:
        idCustomer (AutoField): Primary key for the Customer model.
        accountState (CharField): State of the customer's account.
        personalPresentation (TextField): Personal presentation of the customer.
        idUser (OneToOneField): Foreign key linking to the User model.
    """

    idCustomer = models.AutoField(primary_key=True)
    accountState = models.CharField(max_length=9, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], null=True)
    personalPresentation = models.TextField(null=True)
    idUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the Customer model.

        Returns:
            str: Email of the associated user.
        """
        return self.idUser.email