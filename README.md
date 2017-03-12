# X-Ray

Site web de X-Ray, la radio des élèves de l'Ecole polytechnique.

## Fonctionnalités
- play/pause function
- now playing informations
- sleep mode : volume decreases smoothly and eventually the radio stops playing
- gestion des émissions
- gestion des épisodes
- gestion de la grille musicale

## Projet

Projet basé sur Django.
Librairies additionnelles : jQuery, Wavesurfer.js, FontAwesome, Sass


## Développeurs

Vous devez avoir Python 3 installé (testé avec Python 3.5) et pip
```
git clone <repo_url>
cd backend
pip install -r requirements.txt
```
Ensuite, pour initialiser la base de données et charger les données, tapez :
```
python manage.py migrate
python manage.py loaddata db.json
```
Finalement, lancez le serveur de développement avec :
```
python manage.py runserver
```
Assurez-vous d'avoir un compilateur Sass valide, qui transforme `style.scss` en `../style.css`.
