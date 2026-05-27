from django.db import models
from django.contrib.auth.models import AbstractUser
# PATIENT MODEL
class Patient(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    disease=models.CharField(max_length=50)
    phone=models.IntegerField()

    def __str__(self):
        return self.name
    
# DOCTOR MODEL 

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
# APPOINTMENT MODEL

class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str (self.patient)

