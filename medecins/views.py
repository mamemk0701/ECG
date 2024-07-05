from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AppointmentForm, ConsultationForm
from patients.forms import PatientForm
from .models import Medecin, Appointment, Consultation
from patients.models import Patient


def medecin_login_view(request):
    if request.method == 'POST':
        # Logique de vérification des identifiants, etc.
        return redirect(reverse('dashboard'))  # Exemple de redirection vers le tableau de bord des médecins
    return render(request, 'medecins/medecin_login.html')  # Assurez-vous de créer ce template

def dashboard_view(request):
    return render(request, 'medecins/dashboard.html')

def create_patient(request):  # Renommez la vue en fonction du contexte
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Redirigez vers la liste des patients après création
    else:
        form = PatientForm()
    return render(request, 'medecins/create_patient.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'medecins/patient_list.html', {'patients': patients})

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'medecins/create_appointment.html', {'form': form})

def create_consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('consultation_list')
    else:
        form = ConsultationForm()
    return render(request, 'medecins/create_consultation.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'medecins/appointment_list.html', {'appointments': appointments})

def consultation_list(request):
    consultations = Consultation.objects.all()
    return render(request, 'medecins/consultation_list.html', {'consultations': consultations})
