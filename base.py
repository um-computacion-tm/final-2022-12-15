from persona import Persona


class Base:

    def __init__(self, data=[]):
        self.data = data

    def __repr__(self):
        return f'{self.data}'

    def add(self, persona: Persona):
        self.data.append(persona)

    def sorted(self):
        count = len(self.data)
        for i in range(count - 1):
            for j in range(i + 1, count):
                if self.data[i].nacimiento.compare_to(self.data[j].nacimiento) > 0:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
