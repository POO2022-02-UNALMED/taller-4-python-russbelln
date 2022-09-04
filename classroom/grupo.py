

from .asignatura import Asignatura



class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos =lista+ [alumno]
    
    def __str__(self) -> str:
        cadena = "Grupo de estudiantes: "+self._grupo
        return cadena



    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre


