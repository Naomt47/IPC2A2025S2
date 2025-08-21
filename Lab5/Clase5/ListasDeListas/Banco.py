from ListaCliente import ListaCliente

class Banco: 
    def __init__(self, id, nombre, direccion, antiguedad, sucursales):
        self.id = id
        self.nombre = nombre 
        self.direccion = direccion 
        self.antiguedad = antiguedad
        self.sucursales = sucursales
        self.clientes = ListaCliente()

        self.anterior = None
        self.siguiente = None
        