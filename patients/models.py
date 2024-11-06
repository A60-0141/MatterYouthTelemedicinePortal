from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    viral_load = models.FloatField(null=True, blank=True)  # For HIV patients
    recommendations = models.TextField()
    medication = models.CharField(max_length=255)
    next_appointment = models.DateField(null=True, blank=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.patient.user.username}'s Appointment on {self.appointment_date}"

class GroupChat(models.Model):
    participants = models.ManyToManyField(Patient)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



class Progress(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    health_score = models.IntegerField()  # e.g., 0-100 scale
    doctor_notes = models.TextField()

