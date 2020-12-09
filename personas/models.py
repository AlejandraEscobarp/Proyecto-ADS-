from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class Usuario(AbstractUser):
    OPCIONES_TIPO = (
        ("E", "Estudiante"),
        ("M", "Profesor"),
        ("A", "Administrador"),
        ("P", "Padre de familia"),
    )
    tipo = models.CharField(
        max_length=1,
        choices=OPCIONES_TIPO,
        help_text="Escoja el tipo de usuario a utilizar",
    )

    def es_estudiante(self):
        return self.tipo == "E"

    def es_profesor(self):
        return self.tipo == "M"

    def es_administrador(self):
        return self.tipo == "A"

    def es_padre_de_familia(self):
        return self.tipo == "P"

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Estudiante(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name="estudiante"
    )
    seccion = models.ForeignKey(
        "escuela.Seccion",
        on_delete=models.CASCADE,
        related_name="estudiantes",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.usuario}"

    def clean(self):
        cleaned_data = super().clean()
        if not self.usuario.es_estudiante():
            raise ValidationError(
                "El usuario no es un estudiante, escoja un estudiante"
            )


class PadreDeFamilia(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name="padre_de_familia"
    )
    hijo = models.ManyToManyField(
        Estudiante, through="Familia", verbose_name="estudiantes a cargo"
    )

    def __str__(self):
        return f"{self.usuario}"

    def clean(self):
        cleaned_data = super().clean()
        if not self.usuario.es_padre_de_familia():
            raise ValidationError(
                "El usuario no es un padre de familia, escoja un padre de familia."
            )


class Familia(models.Model):
    OPCIONES_RELACION = (
        ("P", "Padre"),
        ("M", "Madre"),
        ("T", "Tío/Tía"),
        ("A", "Abuelo/Abuela"),
        ("O", "Otro"),
    )
    relacion = models.CharField(
        max_length=1,
        choices=OPCIONES_RELACION,
        help_text="Relación del tutor con el estudiante.",
    )
    tutor = models.ForeignKey(PadreDeFamilia, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)


class Profesor(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name="profesor"
    )

    def __str__(self):
        return f"{self.usuario}"

    def clean(self):
        cleaned_data = super().clean()
        if not self.usuario.es_profesor():
            raise ValidationError(
                "El usuario no es un profesor, escoja un padre profesor."
            )