import os
from Curso import Curso
from graphviz import Digraph  # Importamos para Método 2


class ListaCircularDoble:
    def __init__(self):
        self.primero=None
        self.ultimo=None











    def estaVacia(self):
        """if self.primero==None:
            return True
        else:
            return False"""
        return self.primero==None #sel.primero == self.ultimo == None













    def agregarPrimero(self, codigo, nombre, creditos):
        nuevo=Curso(codigo, nombre, creditos)

        if self.estaVacia():
            self.primero=self.ultimo=nuevo
        else:
            temp=nuevo
            temp.siguiente=self.primero
            self.primero.anterior=temp
            self.primero=temp

        self .__unirNodos()






    









    def __unirNodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero
















    def agregarUltimo(self, codigo, nombre, creditos):
        nuevo=Curso(codigo, nombre, creditos)

        if self.estaVacia():
            self.primero=self.ultimo=nuevo
        else:
            temp=self.ultimo
            self.ultimo=temp.siguiente=nuevo
            self.ultimo.anterior=temp
        self .__unirNodos()













    def eliminarPrimero(self):
        if self.estaVacia():
            print("ERROR: La lista esta vacia")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            temp = self.primero
            self.primero=self.primero.siguiente
            temp.siguiente = temp.anterior = None
            
        self .__unirNodos()








    def eliminarUltimo(self):
        if self.estaVacia():
            print("ERROR: La lista esta vacia")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            temp = self.ultimo
            self.ultimo=self.ultimo.anterior
            temp.siguiente = temp.anterior = None
            """temp.anterior = None
            temp.siguiente = None"""
        self .__unirNodos()










    def recorrerInicioFin(self):
        temp=self.primero
        while temp: #temp != None
            print(temp.codigo, temp.nombre, temp.creditos)
            temp=temp.siguiente
            if temp==self.primero:
                break

                





    def recorrerFinIncio(self):
        temp=self.ultimo
        while temp:
            print(temp.codigo, temp.nombre, temp.creditos)
            temp=temp.anterior
            if temp==self.ultimo:
                break


    def buscar(self,codigo):

        temp=self.primero
        while temp:
            if temp.codigo==codigo:
                return temp

            temp=temp.siguiente
            if temp==self.primero:
                return None

    def graficarMetodo1(self):
        os.makedirs('Metodo1', exist_ok=True)
        contenido = """
    digraph G { 
        rankdir=LR; 
        node[shape=egg, style=filled, color=khaki, fontname="Century Gothic"];  graph [fontname = "Century Gothic"];
        labelloc="t"; label = "Lista Doble Enlazada - Cursos";
"""     
        temp = self.primero
        while temp:
            #Creacion de nodos
            contenido += f"""
        x{temp.codigo}[dir=both label="Codigo = {temp.codigo} \\nNombre = {temp.nombre} \\nCcreditos = {temp.creditos}"]
        x{temp.codigo} -> x{temp.siguiente.codigo}
        x{temp.codigo} -> x{temp.anterior.codigo}
"""
            
            temp=temp.siguiente
            if temp==self.primero:
                break

        contenido += "\t}"

        file = open("Metodo1/reporte.dot","w")
        file.write(contenido)
        file.close()
        print("Grafica Creada con metodo 1")
        os.system("dot -Tpng Metodo1/reporte.dot -o Metodo1/reporte.png")
        os.system("dot -Tpdf Metodo1/reporte.dot -o Metodo1/reporte.pdf")
    

    def graficarMetodo2(self):
        if self.estaVacia():
            print("ERROR: La lista esta vacia")
            return
        
        g = Digraph('G')
        g.attr(rankdir='LR')
        g.attr('node', shape='egg', style='filled', color='khaki', fontname='Century Gothic')
        g.attr(fontname='Century Gothic')
        g.attr(labelloc='t')
        g.attr(label='Lista Doble Enlazada - Cursos')
        
        # Primera pasada: Agregar nodos
        temp = self.primero
        while True:
            node_id = f"x{temp.codigo}"
            g.node(node_id, label=f"Codigo ={temp.codigo}\\nNombre = {temp.nombre} \\nCreditos = {temp.creditos}", dir='both')
            temp = temp.siguiente
            if temp == self.primero:
                break
        
        # Segunda pasada: Agregar aristas
        temp = self.primero
        while True:
            node_id = f"x{temp.codigo}"
            next_id = f"x{temp.siguiente.codigo}"
            prev_id = f"x{temp.anterior.codigo}"
            g.edge(node_id, next_id)
            g.edge(node_id, prev_id)
            temp = temp.siguiente
            if temp == self.primero:
                break
        
        # Renderizar
        os.makedirs('Metodo2', exist_ok=True)
        g.render('Metodo2/reporte', format='png')
        g.render('Metodo2/reporte', format='pdf')
        print("Grafica Creada con Método 2")
    