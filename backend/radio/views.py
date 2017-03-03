from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.template import loader
from django.shortcuts import get_object_or_404

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
    animateurs = Animateur.objects.all()
    templateURL = 'radio/animateurs.html'
    context = {'animateurs' : animateurs}

    return render(request, templateURL, context)

def animateur_details(request, animateur_id):
    # try:
    #     animateurs = Animateur.objects.filter(pk=animateur_id)
    #     context = {'animateur': animateurs[0]}
    # except DoesNotExist:
    #     raise Http404("Animateur does not exist")
    # return render(request, 'radio/animateur-details.html', context)
    animateur = get_object_or_404(Animateur, pk=animateur_id)
    return render(request, 'radio/animateur-details.html', {'animateur': animateur})

def emissions_liste(request):
    return JsonResponse(Emission.objects.all())

def emission_details(request, emission_id):
    return JsonResponse(Emission.objects.filter(pk=emission_id))
