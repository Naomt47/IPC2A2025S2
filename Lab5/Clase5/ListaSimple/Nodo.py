
#NODO
class Cliente: 
    def __init__(self, nombre, cui, saldo, edad):
        
        #DATO
        self.nombre = nombre
        self.cui = cui
        self.saldo =saldo
        self.edad = edad 
        
        
        #APUNTADORES
        self.siguiente = None
