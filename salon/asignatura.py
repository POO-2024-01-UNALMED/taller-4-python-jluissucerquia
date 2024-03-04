class Asignatura:

    def __init__(self, nombreAsignatura, salon = "remoto"):
        self._nombreAsignatura = nombreAsignatura
        self._salon = salon

    def __str__(self):
        return self._nombreAsignatura + "" + self._salon
