from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
