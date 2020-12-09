from django.db import models

from personas.models import Estudiante, Profesor


class Inasistencia(models.Model):
    OPCIONES_TIPO = (
        ("I", "Inasistencia a clase"),
        ("T", "Llegada tardía"),
    )
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo = models.CharField(max_length=1, choices=OPCIONES_TIPO)
    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.CASCADE,
        help_text="Profesor que ha registrado la falta.",
    )

    def __str__(self):
        return f"{self.estudiante}"
