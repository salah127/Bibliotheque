from django.db import models


class Auteur(models.Model):
	nom = models.CharField(max_length=100)
	date_naissance = models.DateField()

	def __str__(self):
		return self.nom

class Livre(models.Model):
	titre = models.CharField(max_length=200)
	date_sortie = models.DateField()
	auteur = models.ForeignKey(Auteur, related_name='livres', on_delete=models.CASCADE)

	def __str__(self):
		return self.titre
