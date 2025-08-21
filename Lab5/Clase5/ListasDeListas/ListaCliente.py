from Cliente import Cliente

class ListaCliente():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return self.primero  == self.ultimo == None
    
    def agregarPrimero(self, nombre, cui, saldo, edad):
        nuevo = Cliente(nombre, cui, saldo, edad)
        if self.estaVacia() == True:
            self.primero  = self.ultimo = nuevo
        else:
            temp = nuevo
            temp.siguiente = self.primero
            self.primero = temp
        
    def agregarUltimo(self, nombre, cui, saldo, edad):
        nuevo = Cliente(nombre, cui, saldo, edad)
        if self.estaVacia() == True:
            self.primero = self.ultimo = nuevo
        else:
            temp = nuevo
            self.ultimo.siguiente = temp
            self.ultimo = temp

    def recorrer(self):
        temp = self.primero
        while temp != None:
            print(temp.cui, temp.nombre, temp.saldo, temp.edad)
            temp = temp.siguiente

    def eliminar(self, cui):
        temp1 = self.primero
        temp2 = None
        while temp1 != None:
            if temp1.cui == cui:
                if temp1 == self.primero:
                    temp2 = self.primero
                    temp1 = temp1.siguiente
                    self.primero = temp1
                    temp2.siguiente = None
                    break
                elif temp1 == self.ultimo: 
                    self.ultimo = temp2
                    temp2.siguiente = None
                    break
                else : 
                    temp2.siguiente = temp1.siguiente
                    temp1.siguiente = None
                    break
            else:
                temp2 = temp1
                temp1 = temp1.siguiente
    
    #SE MODIFICO
    def graficar(self, name):
        temp = self.primero
        contador = 0
        cadena = ""
        while temp != None:
            #cadena += "Nodo"+str(contador)+"[label=\"" + str(temp.cui)+" | "+ temp.nombre+ " | "+ str(temp.precio) + "\"];\n"
            cadena += f"{name}Nodo{contador}[label = \" {temp.nombre} \"]\n"
            if temp != self.primero:
                #cadena += "Nodo"+str(contador-1)+" -> Nodo"+str(contador)+";\n"
                cadena += f"{name}Nodo{contador-1} -> {name}Nodo{contador};\n"
            temp = temp.siguiente
            contador += 1
        
        return cadena


