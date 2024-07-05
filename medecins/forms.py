from django import forms
from .models import Medecin, Appointment, Consultation

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'numero_telephone', 'date_naissance', 'sexe', 'specialite']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'medecin', 'date_heure', 'motif']

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['patient', 'medecin', 'notes', 'fichier_ecg']
