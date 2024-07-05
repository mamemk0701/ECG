from django.db import models
from gestion_ecg.models import Person

class Patient(Person):
    pass  # Ajoutez d'autres attributs spécifiques aux patients si nécessaire

class ECGFile(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    csv_file = models.FileField(upload_to='ecg_files/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ECG de {self.patient} - {self.uploaded_at}"