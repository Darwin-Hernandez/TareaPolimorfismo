class Persona:
    def __init__(self, nombre):
        self.nombre=nombre

    def saludar(self):
        pass

class Alumno(Persona):
       def __init__(self):
            self.nombre="Darwin"
            super().__init__(self.nombre)

       def saludar(self):
            return "hola mi nombre es "+self.nombre

    
class Docente(Persona):

    def __init__(self):
         self.nombre="william"
         super().__init__(self.nombre)

    def saludar(self):
        return "hola mi nombre es " +self.nombre, "y soy el docente"
    
persona1=Alumno()
print(persona1.saludar())
persona2=Docente()
print(persona2.saludar())
