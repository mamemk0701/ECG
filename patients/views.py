from django.shortcuts import render, redirect
from .forms import PatientForm, ECGForm
from medecins.forms import AppointmentForm
from .models import Patient

def patient_login_view(request):
    if request.method == 'POST':
        # Logique de vérification des identifiants, etc.
        return redirect('patients:dashboard')  # Assurez-vous que 'dashboard' est bien défini dans vos URLs
    return render(request, 'patients/patients_login.html')  # Assurez-vous que ce chemin est correct

def dashboard_view(request):
    # Logique pour afficher le tableau de bord
    return render(request, 'patients/dashboard.html')

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'patients/create_appointment.html', {'form': form})

def upload_ecg(request):
    if request.method == 'POST':
        form = ECGForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = ECGForm()
    return render(request, 'patients/upload_ecg.html', {'form': form})
