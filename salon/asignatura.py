class Asignatura:

    def _init_(self, nombreAsignatura, salon = "Remoto"):
        self._nombreAsignatura = nombreAsignatura
        self._salon = salon

    def _str_(self):
        return self._nombreAsignatura + "" + self._salon
