from fecha import Fecha


class Persona:

    def __init__(self, apellido='', nombre='', nacimiento=Fecha()):
        self.apellido = apellido
        self.nombre = nombre
        self.nacimiento = nacimiento

    def __repr__(self):
        return f'{self.apellido}, {self.nombre} / {self.nacimiento}'
