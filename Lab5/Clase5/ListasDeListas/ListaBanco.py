import os
from Banco import Banco


class ListaBanco:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    #----------------- METODOS PARA MODIFICAR LA LISTA "ENCABEZADO" -----------------

    def estaVacio(self):
        return self.primero == self.ultimo == None
    
    def agregarPrimero(self, id, nombre, direccion, antiguedad, sucursales):
        nuevo = Banco(id, nombre, direccion, antiguedad, sucursales)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
    
    def agregarUltimo(self, id, nombre, direccion, antiguedad, sucursales):
        nuevo = Banco(id, nombre, direccion, antiguedad, sucursales)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
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
    
    #SE MODIFICAN LOS METODOS RECORRER Y GRAFICAR
    def recorrer(self):
        temp = self.primero
        while temp!=None:
            print(temp.id, temp.nombre, temp.direccion, temp.antiguedad, temp.sucursales)
            print("LISTA DE CLIENTES")
            temp.clientes.recorrer()
            print("---------------------")
            temp = temp.siguiente
    

    def graficar(self):
        temp = self.primero
        contador = 0
        file = open("ListaDoble.dot", "w")
        cadena = "digraph G{ \n"
        cadena += "rankdir=TB\n"
        cadena += "node[ style=\"filled\", color=\"black\", fillcolor=\"yellow\"];\n"
        while temp!=None:
            cadena += 'Nodo'+str(contador)+'[label="'+temp.nombre+'"];\n'

            #SE OBTIENEN LISTA CLIENTES
            cadena += temp.clientes.graficar(f"Banco{temp.id}")

            #ENLACE DE NODO BANCO AL PRIMER NODO DE LISTA CLIENTES 
            cadena += 'Nodo'+str(contador)+ '-> '+f"Banco{temp.id}Nodo0;\n"
            
            if temp != self.primero:
                cadena += 'Nodo'+str(contador-1)+' -> Nodo'+str(contador)+';\n'
                cadena += 'Nodo'+str(contador)+' -> Nodo'+str(contador-1)+';\n'
            temp = temp.siguiente
            contador += 1

        cadena += 'rank = same {'
        for i in range(contador):
            cadena += 'Nodo'+str(i)+" "
        cadena += '}\n'

        file.write(cadena+"}")
        file.close()
        os.system("dot -Tpng ListaDoble.dot -o listaDoble.png")


    #------------------- NUEVOS METODOS(PARA MANEJAR LAS LISTAS DE CADA NODO) -------------------
    def buscarBanco(self, nombre): #puede ser por id o por cualquier campo que quieran
        temp = self.primero
        while temp !=None:
            if temp.nombre == nombre:
                return temp
            temp = temp.siguiente
        
        return None

    def agregarCliente(self, nombreBanco, nombreCliente, cui, saldo, edad):
        banco = self.buscarBanco(nombreBanco) #encontrar el banco al que queremos insertar el cliente
        if banco != None:
            #Clientes es nuestra simple (insertar, eliminar, graficar)
            banco.clientes.agregarUltimo(nombreCliente, cui, saldo, edad)
        else:
            print(f"No existe el Banco {nombreBanco}")
    
    def eliminarCliente(self, nombreBanco, cui):
        banco = self.buscarBanco(nombreBanco)
        if banco != None:
            banco.clientes.eliminar(cui)
        else:
            print(f"No existe el Banco {nombreBanco}")
