from django.db import models

class Person(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=15)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nom} {self.prenom}"
