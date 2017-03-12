from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views import generic
from django.http import HttpResponse

from .models import Animateur, Emission, Enregistrement, Programme
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'radio/index.html'

def directView(request):
    return render(request, 'index.html', {})

class AnimateursListeView(generic.ListView):
    model = Animateur
    template_name = 'radio/animateurs.html'
    context_object_name = 'animateurs'

class AnimateurDetailsView(generic.DetailView):
    model = Animateur
    template_name = 'radio/animateur-details.html'
    def get_context_data(self, **kwargs):
        context = super(AnimateurDetailsView, self).get_context_data(**kwargs)
        context['ses_derniers_enregistrements'] = Enregistrement.objects.filter(emission__contributeurs__id=context['animateur'].id)

        return context

class AnimateurEmissionsView(generic.ListView):
    model = Emission
    template_name = 'radio/animateur-emissions.html'

class EmissionsListeView(generic.ListView):
    model = Emission
    template_name = 'radio/emissions.html'
    context_object_name = 'emissions'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(EmissionsListeView, self).get_context_data(**kwargs)
    #     for emission in context['emissions']:
    #         emission.derniers_enregistrements = Enregistrement.objects.filter(emission_id = emission.id).order_by('-date_diffusion')

class EmissionDetailsView(generic.DetailView):
    model = Emission
    template_name = 'radio/emission-details.html'

    def get_context_data(self, **kwargs):
        context = super(EmissionDetailsView, self).get_context_data(**kwargs)
        context['derniers_enregistrements'] = Enregistrement.objects.filter(emission_id = context['emission'].id).order_by('-date_diffusion')
        return context

class EmissionAnimateursView(generic.ListView):
    model = Animateur
    template_name = 'radio/emission-animateurs.html'

class EnregistrementListeView(generic.ListView):
    model = Enregistrement
    template_name = 'radio/enregistrements.html'
    context_object_name = 'enregistrements'
    def get_queryset(self):
        return Enregistrement.objects.order_by('-date_diffusion')

def ProgrammeView(request):
    template_name = 'radio/programmes.html'
    tous = Programme.objects.filter(jour=Programme.TOUS).order_by('heure_debut')
    lundi = Programme.objects.filter(jour=Programme.LUNDI).order_by('heure_debut')
    mardi = Programme.objects.filter(jour=Programme.MARDI).order_by('heure_debut')
    mercredi = Programme.objects.filter(jour=Programme.MERCREDI).order_by('heure_debut')
    jeudi = Programme.objects.filter(jour=Programme.JEUDI).order_by('heure_debut')
    vendredi = Programme.objects.filter(jour=Programme.VENDREDI).order_by('heure_debut')
    samedi = Programme.objects.filter(jour=Programme.SAMEDI).order_by('heure_debut')
    dimanche = Programme.objects.filter(jour=Programme.DIMANCHE).order_by('heure_debut')
    data = [
        {'jour': 'tous les jours', 'programmes': tous},
        {'jour': 'lundi', 'programmes': lundi},
        {'jour': 'mardi', 'programmes': mardi},
        {'jour': 'mercredi', 'programmes': mercredi},
        {'jour': 'jeudi', 'programmes': jeudi},
        {'jour': 'vendredi', 'programmes': vendredi},
        {'jour': 'samedi', 'programmes': samedi},
        {'jour': 'dimanche', 'programmes': dimanche}
    ]
    # grille = {}
    # s = ""
    # for programme in Programme.objects.all():
    #     jour = programme.jour
    #     s += "  >jour:" + jour
    #     s += ">titre:" + programme.titre
    #     if jour in grille:
    #         grille[jour][programme.id] = programme
    #     else:
    #         grille[jour] = {programme.id: programme}


    return render(request, template_name,{'data': data})

class EnregistrementDetailView(generic.DetailView):
    model = Enregistrement
    template_name = 'radio/enregistrement-details.html'

def faqView(request):
    template_name = 'radio/participer.html'
    contact = get_object_or_404(Animateur, role="Prez")
    return render(request, template_name, {"contact": contact})

def enregistrement_details(request, emission_id, edition_id):
    #enreg = Enregistrement.objects.filter(emission_id=emission_id, edition_id=edition_id)
    enregistrement = get_object_or_404(Enregistrement, emission_id=emission_id, edition_id=edition_id)
    return render(request, 'radio/enregistrement-details.html', {'enregistrement' : enregistrement})


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
