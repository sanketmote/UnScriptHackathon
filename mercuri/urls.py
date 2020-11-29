from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='mercuri'

urlpatterns = [
    path('addPatient', views.addPatient.as_view(), name="addPatient"),
    path('addDoctor', views.addDoctor.as_view(), name="addDoctor"),
    path('addStaff', views.addStaff.as_view(), name="addStaff"),
    path('addReception', views.addReception.as_view(), name="addReception"),
    path('modifyPatient/<str:mail>', views.modifyPatient.as_view(), name="modifyPatient"),
    path('addHospital', views.addHospital.as_view(), name="addHospital"),
    path('InstanceStatus', views.InstanceStatus.as_view(), name="InstanceStatus"),
    path('Dashboard', views.Dashboard.as_view(), name="Dashboard"),
    path('listPatients', views.listPatients.as_view(), name="listPatients"),
    path('modifyHospital', views.modifyHospital.as_view(), name="modifyHospital"),
    path('addHospital', views.addHospital.as_view(), name="addHospital"),
    path('searchPatient', views.searchPatient.as_view(), name="searchPatient"),
]