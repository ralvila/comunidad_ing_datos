class Animal:

    def __init__(self, nombre):
        self.nombre = nombre


class Perro(Animal):

    def __init__(self, nombre, raza):

        super().__init__(nombre)

        self.raza = raza


mi_perro = Perro("Firulais", "Labrador")

print(mi_perro.nombre)
print(mi_perro.raza)