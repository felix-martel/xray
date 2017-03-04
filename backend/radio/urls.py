from django.conf.urls import url

from . import views

app_name = 'radio'
urlpatterns = [
    url(r'^$', views.directView, name='index'),
    url(r'^direct/$', views.directView, name='direct'),
    url(r'^animateurs/$', views.AnimateursListeView.as_view(), name='animateurs_liste'),
    url(r'^animateurs/(?P<pk>[0-9]+)/$', views.AnimateurDetailsView.as_view(), name='animateur_details'),
    url(r'^animateurs/(?P<pk>[0-9]+)/emissions/$', views.AnimateurEmissionsView.as_view(), name='animateur-emissions'),

    url(r'^emissions/$', views.EmissionsListeView.as_view(), name='emissions_liste'),
    url(r'^emissions/(?P<pk>[0-9]+)/$', views.EmissionDetailsView.as_view(), name='emission_details'),
    url(r'^emissions/(?P<pk>[0-9]+)/animateurs/$', views.EmissionAnimateursView.as_view(), name='emission-animateurs'),
    url(r'^emissions/(?P<emission_id>[0-9]+)/(?P<enregistrement_id>[0-9]+)/$', views.EnregistrementDetailView.as_view(), name='emission_details'),

    url(r'^enregistrements/$', views.EnregistrementListeView.as_view(), name='enregistrements_liste'),
    url(r'^enregistrements/(?P<pk>[0-9]+)/$', views.EnregistrementDetailView.as_view(), name='enregistrement_details'),
]
