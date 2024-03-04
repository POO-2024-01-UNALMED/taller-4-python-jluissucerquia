from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes = None):
        self._grupo = grupo
        self._asignaturas = asignaturas or []
        self.listadoAlumnos = estudiantes or []
        Grupo.grado = "Grado 12"

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista = None):

        if type(lista) != list:
            self.listadoAlumnos.append(alumno)

        else:
            lista.append(alumno)
            self.listadoAlumnos += lista

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre = "Grado 6"):
        cls.grado = nombre

   
