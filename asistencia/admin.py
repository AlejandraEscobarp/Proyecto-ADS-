from django.contrib import admin

from .models import Inasistencia


class InasistenciaAdmin(admin.ModelAdmin):
    list_display = ["estudiante", "tipo", 'fecha']
    ordering = ["-fecha",]

admin.site.register(Inasistencia, InasistenciaAdmin)
