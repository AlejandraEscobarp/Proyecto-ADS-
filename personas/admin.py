from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Estudiante, PadreDeFamilia, Usuario, Profesor, Familia

UserAdmin.fieldsets += (("Tipo de usuario", {'fields': ["tipo"]}),)

admin.site.register(Usuario, UserAdmin)
admin.site.register(Estudiante)
admin.site.register(PadreDeFamilia)
admin.site.register(Profesor)
admin.site.register(Familia)
