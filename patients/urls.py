from django.urls import path
from . import views

app_name = 'patients'  # Assurez-vous que cette ligne est présente

urlpatterns = [
    path('login/', views.patient_login_view, name='patient_login'),
    path('appointment/create/', views.create_appointment, name='create_appointment'),
    path('ecg/upload/', views.upload_ecg, name='upload_ecg'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
