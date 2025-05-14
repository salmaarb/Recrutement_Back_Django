from django.db import models

from candidats.models import Candidat



class Recruteur(models.Model):
    nom_entreprise = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    poste = models.CharField(max_length=100)
    candidats_vus = models.ManyToManyField(Candidat, blank=True, related_name="recruteurs_interesses")

    def __str__(self):
        return f"{self.nom_entreprise} - {self.poste}"