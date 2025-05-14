from django.db import models

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cv = models.TextField(blank=True)
    competences = models.TextField()

    def __str__(self):
        return self.nom