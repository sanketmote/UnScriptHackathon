from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class studentformView(View):
    
    def get(self, request, template_name='accounts/login.html'):
        return render(request, template_name)