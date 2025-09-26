class Banco: 
    def __init__(self, id, nombre, direccion, antiguedad, sucursales):
        #Nodo
        self.id = id
        self.nombre = nombre 
        self.direccion = direccion 
        self.antiguedad = antiguedad
        self.sucursales = sucursales

        #Apuntadores
        self.anterior = None
        self.siguiente = None