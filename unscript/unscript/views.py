from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout

#Handle the login Parts here With a POST request
class Login(View):
    
    def get(self, request, template_name='accounts/login.html'):
        return render(request, template_name)

    def post(self, request, template_name='accounts/login.html'):
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
#group names: adminman doctor reception staff
        if user is not None:
            login(request, user)
            query_set = Group.objects.filter(user = user)
            context = {}
            context["person"]= user
            for g in query_set:
                context["personGroup"] = g.name
                return render(request, 'index.html', context)
        else:
            args3 = {}
            args3['errorStatement'] = "Invalid Login Credentials. Please Try Again"
            return render(request, template_name, args3)

def logout_user(request):
    logout(request)
    return render(request, 'home.html', {})