import os
class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None


class ListaSimple():
    def __init__(self):
        self.primero = None 
        self.ultimo = None
        self.tamanio = 0 


    def estaVacia(self):
        return self.primero  == self.ultimo == None #if self.primero == None and self.ultimo == None
    
    def agregarPrimero(self, dato):
        nuevo = Nodo(dato=dato)
        if self.estaVacia() == True:
            self.primero  = self.ultimo = nuevo
        else:
            temp = nuevo
            temp.siguiente = self.primero
            self.primero = temp
        self.tamanio += 1
        
    def agregarUltimo(self, dato):
        nuevo = Nodo(dato=dato)
        if self.estaVacia() == True:
            self.primero = self.ultimo = nuevo
        else:
            temp = nuevo
            self.ultimo.siguiente = temp
            self.ultimo = temp
        self.tamanio += 1






    def recorrer(self):
        temp = self.primero
        while temp != None:
            #print(temp.dato, temp.dato.jugador, temp.dato.posX, temp.dato.posY)
            print(temp.dato.jugador, end="")
            if temp.siguiente != None:
                    print(" | ", end="")
            temp = temp.siguiente
        print()

    
    def obtenerPorPosicion(self, posX):
        temp = self.primero
        while temp !=None:
            if temp.dato.posX == posX:
                return temp
            temp = temp.siguiente
        return None
    
    
    def obtenerPorIndice(self, indice):
        if indice < 0 or indice >= self.tamanio:
            return None
        
        temp = self.primero
        contador = 0
        while temp != None:
            if contador == indice:
                return temp.dato
            contador += 1
            temp = temp.siguiente
        return None




