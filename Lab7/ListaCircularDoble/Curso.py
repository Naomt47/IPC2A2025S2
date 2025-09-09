#NODO
class Curso():
    def __init__(self, codigo, nombre, creditos):
        #DATO
        self.codigo=codigo
        self.nombre=nombre
        self.creditos=creditos

        #APUNTADORES
        self.siguiente=None
        self.anterior=None