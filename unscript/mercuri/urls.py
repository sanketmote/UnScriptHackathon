from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='mercuri'

urlpatterns = [
    path('addPatient', views.addPatient.as_view(), name="addPatient"),
    path('addDoctor', views.addDoctor.as_view(), name="addDoctor"),
    path('addStaff', views.addStaff.as_view(), name="addStaff"),
]