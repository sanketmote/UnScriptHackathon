from django.shortcuts import render
from django.views.generic.base import View

#Handle the login Parts here With a POST request
class Login(View):
    
    def get(self, request, template_name='accounts/login.html'):
        return render(request, template_name)

    