class Animales:
    def __init__(self, nombre):
        self.nombre=nombre

    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        return "es un animal salvaje"
        
class perro(Animales):
    def tipo_animal(self):
        return "es un animal domestico"

nuevo_animal=Leon("Aslan")
print(nuevo_animal.tipo_animal())
nuevo_animal2=perro("Conan")
print(nuevo_animal2.tipo_animal())