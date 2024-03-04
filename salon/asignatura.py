class Asignatura:

    def _init_(self, nombre = None, salon = "Remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        return self._nombre + "" + self._salon
