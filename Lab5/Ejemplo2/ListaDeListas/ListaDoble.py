import os
from ListaDeListas.ListaSimple import ListaSimple

class NodoEncabezado:
    def __init__(self, dato=None):
        self.dato = dato #NodoCelda (jugador, posX, posY)

        #Apuntadores
        self.siguiente = None
        self.anterior = None


        
        self.fila = ListaSimple()
        




class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def estaVacio(self):
        return self.primero == self.ultimo == None
    

    
    def agregarPrimero(self,dato):
        nuevo = NodoEncabezado(dato=dato)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        self.tamanio += 1
        return nuevo
        

    def agregarUltimo(self, dato):
        nuevo =NodoEncabezado(dato=dato)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.tamanio += 1
        return nuevo
    

    def recorrer(self):
        temp = self.primero
        while temp!=None:
            print(temp.dato)
            temp = temp.siguiente

    
    ##-------------------------------------------------

    def imprimirMatriz(self):
        temp = self.primero
        while temp != None:
            print(f"{temp.dato.posY}: ", end=" ")
            print(f"{temp.dato.jugador}", end=" | ")
            temp.fila.recorrer()
            if temp.siguiente != None:
                print("  "*2 + "--" * (2 * self.tamanio))
            temp = temp.siguiente

    def ObtenerPorPosicion(self, x, y):
        temp = self.primero
        while temp !=None:
            if temp.dato.posY == y:
                if temp.dato.posX == x:
                    return temp
                celda = temp.fila.obtenerPorPosicion(x)
                
                return celda
            temp = temp.siguiente
        return None
    

