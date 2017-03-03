from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: animateurs/
    url(r'^$', views.animateurs_liste, name="animateurs_liste"),
    # ex: animateurs/4/
    url(r'(?P<animateur_id>[0-9]+)/$', views.animateur_details, name="animateur_details"),
    #
    url(r'^$', views.index, name='index'),
]
