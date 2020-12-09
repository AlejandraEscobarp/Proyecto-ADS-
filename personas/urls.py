from django.urls import path
from django.contrib.auth.views import LoginView

from .views import inicio, InicioEstudiante, InicioPadreDeFamilia, InicioProfesor

app_name = "personas"
urlpatterns = [
    path("", LoginView.as_view()),
    path("incicio/", inicio, name="inicio"),
    path(
        "inicio_estudiante/<int:pk>",
        InicioEstudiante.as_view(),
        name="inicio_estudiante"
    ),
    path(
        "inicio_padre/<int:pk>",
        InicioPadreDeFamilia.as_view(),
        name="inicio_padre"
    ),
    path(
        "inicio_profesor",
        InicioProfesor.as_view(),
        name="inicio_profesor"
    )
]