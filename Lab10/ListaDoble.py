import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
from Nodo import Banco

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacio(self):
        return self.primero == self.ultimo == None

    def agregarUltimo(self, id, nombre, direccion, antiguedad, sucursales):
        nuevo = Banco(id, nombre, direccion, antiguedad, sucursales)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

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
        while temp != None:
            if temp.id == id:
                if temp == self.primero:
                    self.primero = temp.siguiente
                    if self.primero:
                        self.primero.anterior = None
                elif temp == self.ultimo:
                    self.ultimo = temp.anterior
                    self.ultimo.siguiente = None
                else:
                    temp.anterior.siguiente = temp.siguiente
                    temp.siguiente.anterior = temp.anterior
                temp.siguiente = None
                temp.anterior = None
                break
            temp = temp.siguiente

    def recorrer(self):
        temp = self.primero
        while temp != None:
            print(temp.id, temp.nombre, temp.direccion, temp.antiguedad, temp.sucursales)
            temp = temp.siguiente

    def graficar(self):
        temp = self.primero
        contador = 0
        cadena = 'digraph G{'
        while temp != None:
            cadena += f'Nodo{contador}[label="{temp.nombre}"];'
            if temp != self.primero:
                cadena += f'Nodo{contador-1} -> Nodo{contador};'
                cadena += f'Nodo{contador} -> Nodo{contador-1};'
            temp = temp.siguiente
            contador += 1
        cadena += "}"
        file = open("static/ListaDoble.dot", "w")
        file.write(cadena)
        file.close()
        os.system("dot -Tpng static/ListaDoble.dot -o static/listaDoble.png")

    def cargarXML(self, xml_path, parser):
        
        self.primero = self.ultimo = None  # Limpiar la lista
        if parser == "elementtree":
            tree = ET.parse(xml_path)
            root = tree.getroot()
            for banco in root.findall('banco'):
                id = int(banco.find('id').text)
                nombre = banco.find('nombre').text
                direccion = banco.find('direccion').text
                antiguedad = int(banco.find('antiguedad').text)
                sucursales = int(banco.find('sucursales').text)
                self.agregarUltimo(id, nombre, direccion, antiguedad, sucursales)
        
        elif parser == "minidom":
            dom = minidom.parse(xml_path)
            bancos = dom.getElementsByTagName('banco')
            for banco in bancos:
                id = int(banco.getElementsByTagName('id')[0].firstChild.data)
                nombre = banco.getElementsByTagName('nombre')[0].firstChild.data
                direccion = banco.getElementsByTagName('direccion')[0].firstChild.data
                antiguedad = int(banco.getElementsByTagName('antiguedad')[0].firstChild.data)
                sucursales = int(banco.getElementsByTagName('sucursales')[0].firstChild.data)
                self.agregarUltimo(id, nombre, direccion, antiguedad, sucursales)

    def __iter__(self):
        temp = self.primero
        while temp:
            yield temp
            temp = temp.siguiente