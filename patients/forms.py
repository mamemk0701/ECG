from django import forms
from .models import Patient, ECGFile

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'prenom', 'numero_telephone', 'date_naissance', 'sexe']

class ECGForm(forms.ModelForm):
    class Meta:
        model = ECGFile
        fields = ['patient', 'csv_file']

    def clean_csv_file(self):
        csv_file = self.cleaned_data['csv_file']
        # Vérifiez ici les conditions supplémentaires sur le fichier CSV si nécessaire
        return csv_file