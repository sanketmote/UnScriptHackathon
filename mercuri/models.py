from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
#User._meta.get_field('email')._unique = True
# Create your models here.

class Patient(models.Model):
    fName = models.CharField(default = 'Mukesh', max_length=30)
    lName = models.CharField(default = 'Ambani', max_length=30)
    email = models.CharField(default = 'patient@patient.com', max_length=50, unique=True)
    age = models.CharField(default = '000', max_length=3)
    address = models.CharField(default = 'Antilla, Mumbai', max_length=500)
    currentStatus = models.CharField(default = 'Active', max_length=10)
    remarks = models.CharField(default = 'Recovering Steadily', max_length=1200)
    medicalHistory = models.CharField(default = 'Diabetic', max_length=1200)
    ventilator = models.BooleanField()
    contactNo = models.CharField(default = '0000000000', max_length=15)
    patientID = models.CharField(default = 'A1A1A1', max_length=12, unique=True)
    isAlive = models.BooleanField()
    operatedByDoctor = models.CharField(default = 'Vijay Raaz', max_length=60)
    def __str__(self):
        return self.fName + self.lName

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fName = models.CharField(default = 'Mukesh', max_length=30)
    lName = models.CharField(default = 'Ambani', max_length=30)
    title = models.CharField(default = 'ENT Specialist', max_length=60)
    contactNo = models.CharField(default = '0000000000', max_length=15)
    email = models.CharField(default = 'patient@patient.com', max_length=50)
    address = models.CharField(default = 'Antilla, Mumbai', max_length=500)
    doctorID = models.CharField(default = 'A1A1A1', max_length=12)
    shift = models.CharField(default = 'Morning', max_length=20)
    def __str__(self):
        return self.fName + self.lName

class HospitalData(models.Model):
    name = models.CharField(default = 'Mukesh', max_length=100)
    address = models.CharField(default = 'Antilla, Mumbai', max_length=500)
    contactNo = models.CharField(default = '0000000000', max_length=15)
    ventilators = models.CharField(default = '000000', max_length=5)
    beds = models.CharField(default = '000000', max_length=6)
    availableOxygenCylinders = models.CharField(default = '000000', max_length=6)

class HospitalStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fName = models.CharField(default = 'Mukesh', max_length=30)
    title = models.CharField(default = 'Nurse', max_length=60)
    lName = models.CharField(default = 'Ambani', max_length=30)
    staffID = models.CharField(default = 'A1A1A1', max_length=12)
    contactNo = models.CharField(default = '0000000000', max_length=15)
    email = models.CharField(default = 'patient@patient.com', max_length=50)
    address = models.CharField(default = 'Antilla, Mumbai', max_length=500)
    shift = models.CharField(default = 'Morning', max_length=10)
    def __str__(self):
        return self.fName + self.lName

class StatusForChart(models.Model):
    currentActive = models.CharField(default = '000000', max_length=6)
    currentDeceased = models.CharField(default = '000000', max_length=6)
    currentRecovered = models.CharField(default = '000000', max_length=6)

class Reception(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fName = models.CharField(default = 'Mukesh', max_length=30)
    lName = models.CharField(default = 'Ambani', max_length=30)
    staffID = models.CharField(default = 'A1A1A1', max_length=12)
    contactNo = models.CharField(default = '0000000000', max_length=15)
    email = models.CharField(default = 'patient@patient.com', max_length=50)
    address = models.CharField(default = 'Antilla, Mumbai', max_length=500)
    shift = models.CharField(default = 'Morning', max_length=10)
    def __str__(self):
        return self.fName + self.lName

