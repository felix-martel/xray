from django.contrib import admin

# Register your models here.
from .models import Emission, Enregistrement, Animateur, Programme

admin.site.register(Emission)
admin.site.register(Enregistrement)
admin.site.register(Animateur)
admin.site.register(Programme)
