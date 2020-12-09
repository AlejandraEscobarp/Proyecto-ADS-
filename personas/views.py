from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

from .mixins import IsSelfStudentOrGuardian
from .models import Estudiante, PadreDeFamilia, Familia


@login_required
def inicio(request):
    user = request.user
    if user.es_estudiante():
        return redirect(
            reverse("personas:inicio_estudiante", args=(user.estudiante.id,))
        )
    elif user.es_padre_de_familia():
        return redirect(
            reverse("personas:inicio_padre", args=(user.padre_de_familia.id,))
        )
    elif user.es_profesor():
        return redirect(
            reverse("personas:inicio_profesor")
        )
    else:
        return redirect(reverse("admin:index"))


class InicioEstudiante(IsSelfStudentOrGuardian, DetailView):
    queryset = Estudiante.objects.all()
    template_name = "personas/inicio_estudiantes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estudiante = Estudiante.objects.get(pk=self.kwargs["pk"])
        context["estudiante"] = estudiante
        context["inasistencias"] = estudiante.inasistencia_set.all()
        return context


class InicioPadreDeFamilia(LoginRequiredMixin, DetailView):
    queryset = PadreDeFamilia.objects.all()
    template_name = "personas/inicio_padres_de_familia.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "familias"
        ] = Familia.objects.filter(tutor__usuario = self.request.user)
        return context


class InicioProfesor(TemplateView):
    template_name = 'personas/inicio_profesores.html'