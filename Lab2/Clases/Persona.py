class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.genero = "Femenino"

    def saludar(self):
        return f"Hola, yo soy {self.nombre}, tengo {self.edad} años"
    
    def despedirse(self):
        return "Adiós"
    
    

