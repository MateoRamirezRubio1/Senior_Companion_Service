from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from authentication.models import User as UserA

SERVICE_CHOICES = (
    ("Activity Accompaniment", "Activity Accompaniment"),
    ("Housework Support", "Housework Support"),
    ("Companionship and Conversation", "Companionship and Conversation"),
    ("Specialized Companionship", "Specialized Companionship"),
    )
TIME_CHOICES = (
    ("8:00 AM", "8:00 AM"),
    ("8:30 AM", "8:30 AM"),
    ("9:00 AM", "9:00 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10:00 AM", "10:00 AM"),
    ("10:30 AM", "10:30 AM"),
    ("11:00 AM", "11:00 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12:00 PM", "12:00 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1:00 PM", "1:00 PM"),
    ("1:30 PM", "1:30 PM"),
    ("2:00 PM", "2:00 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(UserA, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    names = models.CharField(max_length=80)
    lastNames = models.CharField(max_length=80)
    password = models.CharField(max_length=255, editable=False)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=60, null=True)
    birthDate = models.DateField(null=True)
    genre = models.CharField(
        max_length=6,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        null=True
    )
    email = models.CharField(max_length=60, unique=True, null=False)
    profilePhoto = models.CharField(max_length=200, null=True)
    registrationDate = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=100, null=True)
    class Meta:
        managed = False
        db_table = 'User'


availability = [('disponible', 'disponible'), ('no disponible', 'no disponible'), ('pausa', 'pausa')]

class Companion(models.Model):
    id = models.AutoField(primary_key=True, db_column='idCompanion')
    stateAvailability = models.CharField(max_length =20, choices=availability)
    personalDescription = models.TextField()
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, db_column='idUser')
    class Meta:
        managed = False
        db_table = 'Companion'

states = [('Activo', 'Activo'), ('inactivo', 'inactivo')]

class Customer(models.Model):
    id = models.AutoField(primary_key=True, db_column='idCustomer')
    accountState  = models.CharField(max_length =20, choices=states)
    personalPresentation = models.TextField()
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, db_column='idUser')
    class Meta:
        managed = False
        db_table = 'Customer'


class MedicalInformation(models.Model):
    id = models.AutoField(primary_key=True, db_column='idMedicalInformation')
    allergies = models.TextField()
    medicalConditions = models.TextField()
    medicationIntake = models.TextField()
    medicationRestriction = models.TextField()
    emergencyContact = models.TextField()
    class Meta:
        managed = False
        db_table = 'MedicalInformation'
    


states = [('pending', 'pending'), ('confirmed', 'confirmed'), ('completed', 'completed'), ('cancelled', 'cancelled')]
  
modalities = [('on-site', 'on-site'), ('online', 'online')]
class Reserve(models.Model):
    id = models.AutoField(primary_key=True, db_column='idReserve')
    startTime = models.DateField()
    endDate = models.DateField()
    stateReserve = models.CharField(max_length=45, choices= states)
    creationDate = models.DateField()
    modality = models.CharField(max_length=45, choices=modalities)
    additionalComment = models.TextField()
    idCompanion = models.ForeignKey(Companion, on_delete=models.CASCADE, db_column='idCompanion')
    idCustomer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='idCustomer')
    class Meta:
        managed = False
        db_table='Reserve'





