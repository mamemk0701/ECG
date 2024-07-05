from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create/', views.create_patient, name='create_patient'),
    path('patient/list/', views.patient_list, name='patient_list'),  # Ajoutez cette ligne pour la liste des patients
    path('appointment/create/', views.create_appointment, name='create_appointment'),
    path('appointment/list/', views.appointment_list, name='appointment_list'),
    path('consultation/create/', views.create_consultation, name='create_consultation'),
    path('consultation/list/', views.consultation_list, name='consultation_list'),
    path('login/', views.medecin_login_view, name='medecin_login'),
]