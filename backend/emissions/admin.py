from django.contrib import admin

# Register your models here.
from .models import Emission, Enregistrement

admin.site.register(Emission)
admin.site.register(Enregistrement)
