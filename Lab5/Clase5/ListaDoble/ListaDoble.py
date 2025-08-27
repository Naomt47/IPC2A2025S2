import os
from Nodo import Banco


class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None


    def estaVacio(self):
        return self.primero == self.ultimo == None
    
    

    def agregarUltimo(self, id, nombre, direccion, antiguedad, sucursales):
        #crear el nodo
        nuevo = Banco(id, nombre, direccion, antiguedad, sucursales)
        
        #if self.primero == None and self.ultimo == None
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
            
        else:
            nuevo.anterior = self.ultimo #enlace 1
            self.ultimo.siguiente = nuevo  #enlace 2
            self.ultimo = nuevo


    def recorrer(self):
        temp = self.primero
        while temp!=None:
            print(temp.id, temp.nombre, temp.direccion, temp.antiguedad, temp.sucursales)
            temp = temp.siguiente


    def agregarPrimero(self, id, nombre, direccion, antiguedad, sucursales):
        nuevo = Banco(id, nombre, direccion, antiguedad, sucursales)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo


    def eliminar(self, id):
        temp = self.primero
        while temp!=None:
            if temp.id == id:
                if temp == self.primero:
                    self.primero = temp.siguiente
                    temp.siguiente = None
                    self.primero.anterior = None
                    break
                elif temp == self.ultimo:
                    self.ultimo = temp.anterior
                    temp.anterior = None
                    self.ultimo.siguiente = None
                    break
                else:
                    temp.anterior.siguiente = temp.siguiente
                    temp.siguiente.anterior = temp.anterior
                    temp.siguiente = None
                    temp.anterior = None
                    break
            temp = temp.siguiente
    
    
    def graficar(self):
        temp = self.primero
        contador = 0
        cadena = 'digraph G{'
        file = open("ListaDoble.dot", "w")
        while temp!=None:
            cadena += 'Nodo'+str(contador)+'[label="'+temp.nombre+'"];'
            if temp != self.primero:
                cadena += 'Nodo'+str(contador-1)+' -> Nodo'+str(contador)+';'
                cadena += 'Nodo'+str(contador)+' -> Nodo'+str(contador-1)+';'
            temp = temp.siguiente
            contador += 1
        file.write(cadena+"}")
        file.close()
        os.system("dot -Tpng ListaDoble.dot -o listaDoble.png")