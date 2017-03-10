from django.db import models

# Create your models here.
class Animateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    surnom = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    presentation = models.TextField(default="")
    allow_contact = models.BooleanField(default=False)
    email = models.EmailField(null=True)

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
    description = models.TextField()
    dernier_episode = models.ForeignKey('Enregistrement', null=True, related_name='+')

    def __str__(self):
        return self.nom

class Enregistrement(models.Model):
    emission = models.ForeignKey(Emission)
    edition_id = models.SmallIntegerField()
    titre = models.CharField(max_length=200)
    emission_url = models.CharField(max_length=200, default='demo.wav')
    date_diffusion = models.DateTimeField()
    description = models.TextField()
    def __str__(self):
        return self.emission.nom + " du " + self.date_diffusion.strftime('%d/%m')
