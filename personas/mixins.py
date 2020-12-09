from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Estudiante, Familia
from escuela.models import Seccion


class IsSelfStudentOrGuardian(UserPassesTestMixin):
    """
    Determina si un usuario puede ver la información de un estudiante porque:
    - Es el mismo estudiante
    - Es un profesor que le da clases al estudiante
    - Es un padre de familia a cargo del estudiante
    """

    def test_func(self):
        """
        Retorna True si cumple alguna de las funcione del Mixin
        """
        if self.request.user.es_administrador():
          return True
        elif self.request.user.es_estudiante():
            return self.request.user.estudiante.id == self.kwargs["pk"]
        elif self.request.user.es_profesor():
          estudiante = Estudiante.objects.get(estudiante_id=self.kwargs["pk"])
          seccion = estudiante.seccion
          return self.user.profesor in seccion.profesores
        elif self.request.user.es_padre_de_familia():
          familias = Familia.objects.filter(estudiante_id=self.kwargs["pk"])
          for familia in familias:
            if self.request.user.padre_de_familia == familia.tutor:
              return True
            return False
        else:
          return False


