from django.db import models
from authentication.models import User

class Companion(models.Model):
    """
    Model for representing a companion.

    Attributes:
        idCompanion (AutoField): Primary key for the Companion model.
        stateAvailability (CharField): Availability state of the companion.
        hourlyRate (DecimalField): Hourly rate of the companion.
        personalDescription (TextField): Personal description of the companion.
        idUser (OneToOneField): Foreign key linking to the User model.
    """

    idCompanion = models.AutoField(primary_key=True)
    stateAvailability = models.CharField(max_length=15, choices=[('available', 'Available'), ('not available', 'Not Available'), ('pause', 'Pause'), ('blocked', 'Blocked')], null=True)
    hourlyRate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    personalDescription = models.TextField(null=True)
    idUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the Companion model.

        Returns:
            str: Email of the associated user.
        """
        return self.idUser.email