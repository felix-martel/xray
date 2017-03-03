from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

import json
from .models import Animateur, Emission, Enregistrement
# Create your views here.

def JsonResponse(data):
    """
    @param data : QuerySet
    """
    return HttpResponse(serializers.serialize('json', data), content_type="json")

def index(request):
    return HttpResponse("Index des émissions")

def animateurs_liste(request):
    return JsonResponse(Animateur.objects.all())

def animateur_details(request, animateur_id):
    return JsonResponse(Animateur.objects.filter(pk=animateur_id))

def emissions_liste(request):
    return JsonResponse(Emission.objects.all())

def emission_details(request, emission_id):
    return JsonResponse(Emission.objects.filter(pk=emission_id))
