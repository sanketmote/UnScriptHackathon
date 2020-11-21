from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from mercuri.models import Patient as Patient
# Create your views here.
class addPatient(View):
    
    def get(self, request, template_name='addPatient.html'):
        return render(request, template_name)

    def post(self, request, template_name='addPatient.html'):
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        fullName = fName + " " + lName
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        currentStatus = request.POST.get('currentStatus')
        remarks = request.POST.get('remarks')
        medicalHistory = request.POST.get('medicalHistory')
        ventilator = True
        contactNo = request.POST.get('contactNo')
        patientID = request.POST.get('patientID')
        isAlive = True
        operatedByDoctor = request.POST.get('operatedByDoctor')
        try:
            addPat = Patient(fName=fName, lName=lName, fullName=fullName, email=email, age=age, address=address, currentStatus=currentStatus, remarks=remarks, medicalHistory=medicalHistory, ventilator=ventilator, contactNo=contactNo, patientID=patientID, isAlive=isAlive, operatedByDoctor=operatedByDoctor)
            addPat.save()
            err = {'error_message': "Patient Added Successfully."}
        except:
            err = {'error_message': "Some Error Occurred. Please Try Again"}
        
        return render(request, template_name, err)
