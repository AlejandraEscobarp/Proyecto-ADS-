from django.db import models

from personas.models import Estudiante, Profesor


class Seccion(models.Model):
    nivel_educativo = models.CharField(
        max_length=25, help_text="Ingese el nivel educativo de la sección"
    )
    OPCIONES_SECCION = (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"))
    seccion = models.CharField(
        max_length=1,
        verbose_name="sección",
        choices=OPCIONES_SECCION,
        help_text="Sección",
    )
    profesores = models.ManyToManyField(Profesor)

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"
