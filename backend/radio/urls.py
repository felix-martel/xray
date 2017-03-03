from django.conf.urls import url

from . import views

app_name = 'radio'
urlpatterns = [
    # ex: animateurs/
    url(r'^animateurs/$', views.animateurs_liste, name="animateurs_liste"),
    # ex: animateurs/4/
    url(r'^animateurs/(?P<animateur_id>[0-9]+)/$', views.animateur_details, name="animateur_details"),
    # ex: emissions/
    url(r'^emissions/$', views.emissions_liste, name="emissions_liste"),
    # ex: animateurs/4/
    url(r'^emissions/(?P<emission_id>[0-9]+)/$', views.emission_details, name="emission_details"),
    #
    url(r'^$', views.index, name='index'),
]
