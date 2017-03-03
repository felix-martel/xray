from django.db import models

# Create your models here.
class Animateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    surnom = models.CharField(max_length=50)
    role = models.CharField(max_length=100)

    def __str__(self):
        if len(self.surnom) > 0:
            return self.prenom + ' "' + self.surnom + '" ' + self.nom
        else:
            return self.prenom + ' ' + self.nom

class Emission(models.Model):
    nom = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    date_derniere_diffusion = models.DateTimeField("Date de la derniere emission")
    contributeurs = models.ManyToManyField(Animateur)
    def __str__(self):
        return self.nom

class Enregistrement(models.Model):
    emission = models.ForeignKey(Emission)
    titre = models.CharField(max_length=200)
    date_diffusion = models.DateTimeField()
    def __str__(self):
        return self.emission.nom + " du " + self.date_diffusion.strftime('%d/%m')
