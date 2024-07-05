from django.db import models
from patients.models import Patient
from gestion_ecg.models import Person

class Medecin(Person):
    specialite = models.CharField(max_length=100)
    # Ajoutez d'autres attributs spécifiques aux médecins si nécessaire

class Appointment(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()
    motif = models.TextField()

    def __str__(self):
        return f"Rendez-vous avec {self.patient} et {self.medecin} le {self.date_heure}"

class Consultation(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_heure = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()
    fichier_ecg = models.FileField(upload_to='ecg_files/')

    def __str__(self):
        return f"Consultation avec {self.patient} et {self.medecin} le {self.date_heure}"
