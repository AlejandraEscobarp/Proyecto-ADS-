from django.urls import path

from .views import CrearInasistencia

app_name = "asistencia"
urlpatterns = [
  path("crear_inasistencia/", CrearInasistencia.as_view(), name="crear_inasistencia"),
]