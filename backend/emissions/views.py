from django.shortcuts import render
from django.http import HttpResponse
from .models import Animateur
# Create your views here.
def index(request):
    return HttpResponse("Index des émissions")

def animateurs_liste(request):
    result = "Liste des animateurs : \n--\n"
    for anim in Animateur.objects.all():
        result += str(anim) + "\n"
    return HttpResponse(result)

def animateur_details(request, animateur_id):
    try:
        a = Animateur.objects.get(pk=animateur_id)
        result = "Nom : {}\nPrénom : {}\nRôle : {}"
        return HttpResponse(result.format(a.nom, a.prenom, a.role))
    except DoesNotExist:
        return HttpResponse("Animateur inconnu")
