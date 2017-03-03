from radio.models import Animateur, Emission, Enregistrement
from django.utils import timezone

a1 = Animateur(nom="Martel", prenom="Félix", surnom="Méxil", role="Prez")
a2 = Animateur(nom="Chevallier-Chantepie", prenom="Pierre Louis", surnom="Chantepax", role="VPrez")
a3 = Animateur(nom="Meary", prenom="Quentin", role="Trez")
a4 = Animateur(nom="Mallet", prenom="Vincent")
a5 = Animateur(nom="Msika", prenom="Simon")
a6 = Animateur(nom="Colin", prenom="Samuel")
a7 = Animateur(nom="Membrado", prenom="Jean-Baptiste")

a1.save()
a2.save()
a3.save()
a4.save()
a5.save()
a6.save()
a7.save()

e = Emission(nom="La Tête dans le GU", date_derniere_diffusion=timezone.now())
e.save()
e.contributeurs.add(a2)
