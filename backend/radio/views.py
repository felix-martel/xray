from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views import generic


from .models import Animateur, Emission, Enregistrement
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

class EnregistrementDetailView(generic.DetailView):
    model = Enregistrement
    template_name = 'radio/enregistrement-details.html'

def faqView(request):
    template_name = 'radio/faq.html'
    return render(request, template_name, {})

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
