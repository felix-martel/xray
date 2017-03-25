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

class Album(models.Model):
    nom = models.CharField(max_length=200)
    album_art = models.CharField(max_length=200, blank=True, default='')
    artiste = models.CharField(max_length=200)
    annee = models.CharField(max_length=4)
    date_creation = models.DateTimeField("Date d'ajout", auto_now_add=True)
    description = models.TextField()
    lien_phoenix = models.CharField(default = '', max_length=300, blank=True)
    lien_deezer = models.CharField(default = '', max_length=300, blank=True)
    lien_spotify = models.CharField(default = '', max_length=300, blank=True)
    lien_youtube = models.CharField(default = '', max_length=300, blank=True)
    def __str__(self):
        return self.nom + " [" + self.artiste + "](" + self.annee + ")"



class Enregistrement(models.Model):
    emission = models.ForeignKey(Emission)
    edition_id = models.SmallIntegerField()
    titre = models.CharField(max_length=200)
    emission_url = models.CharField(max_length=200, default='demo.wav')
    date_diffusion = models.DateTimeField()
    description = models.TextField()
    def __str__(self):
        return self.emission.nom + " du " + self.date_diffusion.strftime('%d/%m')

class Programme(models.Model):
    titre = models.CharField(max_length=200, blank=True, default="")
    description = models.TextField()
    heure_debut = models.DateTimeField()
    heure_fin = models.DateTimeField()
    playlist_id = models.CharField(max_length=200, blank=True, default="")
    TOUS = '00TS'
    LUNDI = '01LU'
    MARDI = '02MA'
    MERCREDI = '03ME'
    JEUDI = '04JE'
    VENDREDI = '05VE'
    SAMEDI = '06SA'
    DIMANCHE = '07DI'
    jours_de_la_semaine = (
        (TOUS, 'Tous les jours'),
        (LUNDI, 'Lundi'),
        (MARDI, 'Mardi'),
        (MERCREDI, 'Mercredi'),
        (JEUDI, 'Jeudi'),
        (VENDREDI, 'Vendredi'),
        (SAMEDI, 'Samedi'),
        (DIMANCHE, 'Dimanche'),
        (None, 'Choisis un jour'),
    )
    jour = models.CharField(max_length=4, choices=jours_de_la_semaine, default=TOUS)

    def __str__(self):
        return self.titre
