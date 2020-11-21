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
from mercuri.models import Doctor as Doctor
from mercuri.models import HospitalStaff as Staff
from mercuri.models import Reception as Reception
from mercuri.models import HospitalData as HospitalDat
from django.core.files.storage import FileSystemStorage
import shortuuid

# Create your views here.
class addPatient(View):
    
    def get(self, request, template_name='addPatient.html'):
        return render(request, template_name)

    def post(self, request, template_name='addPatient.html'):
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        email = request.POST.get('email')
        email = str(email)
        age = request.POST.get('age')
        age = str(age)
        address = request.POST.get('address')
        currentStatus = "Active"
        remarks = request.POST.get('remarks')
        medicalHistory = request.POST.get('medicalHistory')
        ventilator = False
        contactNo = request.POST.get('contactNo')
        patientID = request.POST.get('patientID')
        isAlive = True
        operatedByDoctor = request.POST.get('operatedByDoctor')
        try:
            addPat = Patient(fName=fName, lName=lName, email=email, age=age, address=address, currentStatus=currentStatus, remarks=remarks, medicalHistory=medicalHistory, ventilator=ventilator, contactNo=contactNo, patientID=patientID, isAlive=isAlive, operatedByDoctor=operatedByDoctor)
            addPat.save()
            err = {'error_message': "Patient Added Successfully."}
        except:
            err = {'error_message': "Some Error Occurred. Please Try Again"}
        
        return render(request, template_name, err)

class addDoctor(View):

    def get(self, request, template_name='addDoctor.html'):
        return render(request, template_name)

    def post(self, request, template_name='addDoctor.html'):
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        email = request.POST.get('email')
        title = request.POST.get('title')
        shift = request.POST.get('shift')
        address = request.POST.get('address')
        contactNo = request.POST.get('contactNo')
        doctorID = request.POST.get('doctorID')
        password = request.POST.get('password')
        confPassword = request.POST.get('confPassword')
        if password != confPassword:
            err = {'error_message': "Passwords don't match. Please Try Again."}
            return render(request, 'addDoctor.html', err)

        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except:
            err = {}
            err['error_message'] = "Account with this Email already Exists."
            return render(request, template_name, err)

        try:
            docData = Doctor(fName=fName, lName=lName, email=email, title=title, shift=shift, address=address, contactNo=contactNo, doctorID=doctorID)
            docData.save()
        except:
            err = {}
            err['error_message'] = "Some Error Occurred. Try Again."
            return render(request, template_name, err)


        my_group = Group.objects.get(name='doctor')
        my_group.user_set.add(user)

        err = {}
        err['error_message'] = "Doctor Added Successfully."
        return render(request, template_name, err)

class addStaff(View):

    def get(self, request, template_name='addStaff.html'):
        return render(request, template_name)

    def post(self, request, template_name='addStaff.html'):
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        email = request.POST.get('email')
        title = request.POST.get('title')
        shift = request.POST.get('shift')
        address = request.POST.get('address')
        contactNo = request.POST.get('contactNo')
        contactNo = str(contactNo)
        staffID = request.POST.get('staffID')
        password = request.POST.get('password')
        confPassword = request.POST.get('confPassword')
        if password != confPassword:
            err = {'error_message': "Passwords don't match. Please Try Again."}
            return render(request, 'addStaff.html', err)

        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except:
            err = {}
            err['error_message'] = "Account with this Email already Exists."
            return render(request, template_name, err)

        try:
            docData = Staff(user=user, fName=fName, lName=lName, email=email, title=title, shift=shift, address=address, contactNo=contactNo, staffID=staffID)
            docData.save()
        except:
            err = {}
            err['error_message'] = "Some Error Occurred. Try Again."
            return render(request, template_name, err)

        my_group = Group.objects.get(name='staff')
        my_group.user_set.add(user)

        err = {}
        err['error_message'] = "Staff Added Successfully."
        return render(request, template_name, err)

class addReception(View):

    def get(self, request, template_name='addReception.html'):
        return render(request, template_name)

    def post(self, request, template_name='addReception.html'):
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        email = request.POST.get('email')
        shift = request.POST.get('shift')
        address = request.POST.get('address')
        contactNo = request.POST.get('contactNo')
        staffID = request.POST.get('staffID')
        password = request.POST.get('password')
        confPassword = request.POST.get('confPassword')
        if password != confPassword:
            err = {'error_message': "Passwords don't match. Please Try Again."}
            return render(request, 'addReception.html', err)

        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except:
            err = {}
            err['error_message'] = "Account with this Email already Exists."
            return render(request, template_name, err)
        
        try:
            docData = Reception(user=user, fName=fName, lName=lName, email=email, shift=shift, address=address, contactNo=contactNo, staffID=staffID)
            docData.save()
        except:
            err = {}
            err['error_message'] = "Some Error Occurred. Try Again."
            return render(request, template_name, err)

        my_group = Group.objects.get(name='reception')
        my_group.user_set.add(user)

        err = {}
        err['error_message'] = "Reception Added Successfully."
        return render(request, template_name, err)

class ModifyPatient(View):
    def get(self, request, template_name='modifyPatient.html'):
        return render(request, template_name)

    def post(self, request, template_name='modifyPatient.html'):
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        currentStatus = request.POST.get('currentStatus')
        remarks = request.POST.get('remarks')
        medicalHistory = request.POST.get('medicalHistory')
        ventilator = request.POST.get('ventilator')
        contactNo = request.POST.get('contactNo')
        patientID = request.POST.get('patientID')
        isAlive = request.POST.get('isAlive')
        operatedByDoctor = request.POST.get('operatedByDoctor')

        Patient.objects.filter(fName=fName, lName=lName, email=email, age=age, address=address, contactNo=contactNo, medicalHistory=medicalHistory).update(currentStatus=currentStatus, remarks=remarks, ventilator=ventilator, contactNo=contactNo, patientID=patientID, isAlive=isAlive, operatedByDoctor=operatedByDoctor)
        return render(request, template_name, {"err": "Changes Done Successfully"})

class addHospital(View):

        def get(self, request, template_name='hospital.html'):
            return render(request, template_name)

        def post(self, request, template_name='hospital.html'):
            name = request.POST.get('name')
            address = request.POST.get('address')
            contactNo = request.POST.get('contactNo')
            ventilators = request.POST.get('ventilators')
            beds = request.POST.get('beds')
            occupiedVentilators = request.POST.get('occupiedVentilators')
            occupiedBeds = request.POST.get('occupiedBeds')
            availableOxygenCylinders = request.POST.get('availableOxygenCylinders')
            err = {}
            try:
                addHospital2 = HospitalDat(name=name, address=address, contactNo=contactNo, ventilators=ventilators, beds=beds, occupiedBeds=occupiedBeds, occupiedVentilators=occupiedVentilators, availableOxygenCylinders=availableOxygenCylinders)
                addHospital2.save()
                err["errorMessage"] = "Hospital Added Successfully"
            except:
                err["errorMessage"] = "Some Error Occurred. Please Try Again"

            return render(request, template_name, err)