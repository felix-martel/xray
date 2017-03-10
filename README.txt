HEBERGEMENT DES SITES BINETS

1. accès ftp
Le dossier www contient tous les sites qui appartiennent à un binet dont vous
êtes administrateur.
Tous les sites du BR sont dans www/br
Si votre binet n'a qu'un site, il est normalement dans www/<nom du
binet>/htdocs. Sinon, lors de la création de votre site, le nom du dossier a
du vous être communiqué.

2. accès ssh
L'accès ssh vous donne beaucoup de pouvoir, mais est très pratique. Nous
comptons sur vous pour ne pas en abuser, sans quoi cette expérience prendrait
fin.
La racine du ftp est /hosting. Donc les sites sont dans /hosting/www/<nom du
binet>/htdocs ou assimilé.
Votre dossier personnel est dans /hosting/users/<login frankiz>
Il y a des quotas (stricts) d'espace disque : 
* chaque binet correspond à un utilisateur et un groupe. Quand vous écrivez
  dans /hosting/www/br par exemple, les fichiers appartiennent automatiquement
  au groupe br. Le groupe a un quota.
* Les dossiers personnels ont aussi un quota. Ne laissez rien dans votre dossier
  personnel.

L'accès à internet est restreint à kuzh uniquement. Les programmes qui
essaient d'accéder à internet sans passer par kuzh peuvent utiliser
proxychains.

3. sites php
Pensez aux .htaccess. Les bases de données sont accessibles à l'adresse
http://phpmyadmin.bin
Les logs sont dans logs/<binet>.

4. sites en django
Les logs sont dans /var/log/uwsgi.
Pour les fichiers statiques, mettre dans settings.py :

STATIC_URL = '/assets/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "assets/static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "assets/media/")
MEDIA_URL = '/assets/media/'

Les fichiers statiques seront dans /hosting/www/<binet>/<site>/assets

Pour les emails (indispensable pour être averti des erreurs 500) :

DEFAULT_FROM_EMAIL = "binet_chombier@binets.polytechnique.fr"
# voir https://portail.polytechnique.edu/dsi/eleves/mail-binets
SERVER_EMAIL = DEFAULT_FROM_EMAIL
ADMINS = [("Webmaster", DEFAULT_FROM_EMAIL)]

Oui, vous pouvez mettre d'importe quelle adresse email dans le champ "From",
non, ne jouez pas à ça. Nous prenons cela au sérieux.

À chaque modification du code python, vous devez lancer la commande : 

touch /var/run/please/restart

pour que la modification soit prise en compte. Cela peut prendre jusqu'à 5
minutes.
