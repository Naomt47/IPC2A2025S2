
#CLASE NODO
class Banco: 
    def __init__(self, id, nombre, direccion, antiguedad, sucursales):
        #DATO
        self.id = id
        self.nombre = nombre 
        self.direccion = direccion 
        self.antiguedad = antiguedad
        self.sucursales = sucursales

        #APUNTADORES
        self.anterior = None
        self.siguiente = None
        