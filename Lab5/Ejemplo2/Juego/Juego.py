import xml.etree.ElementTree as ET
from xml.dom import minidom
from Juego.Tablero import TableroTotito

class JuegoTotito:
    def __init__(self):
        self.tablero = None
        self.jugadorActual = "X"
        self.movimientos = 0
    
    def cargarConfiguracionMinidom(self, archivo):
        """Carga la configuración usando minidom"""
        try:
            doc = minidom.parse(archivo)
            # Obtener configuración
            config = doc.getElementsByTagName("configuracion")[0]
            filas = int(config.getElementsByTagName("filas")[0].firstChild.data)
            columnas = int(config.getElementsByTagName("columnas")[0].firstChild.data)
            self.jugadorActual = config.getElementsByTagName("jugador_inicial")[0].firstChild.data
            
            # Crear tablero con nuestras estructuras
            self.tablero = TableroTotito(filas, columnas)
            self.movimientos = 0
            
            # Cargar movimientos iniciales
            movimientos = doc.getElementsByTagName("movimiento")

            for mov in movimientos:
                fila = int(mov.getAttribute("fila"))
                columna = int(mov.getAttribute("columna"))
                jugador = mov.getAttribute("jugador")
                

                if self.tablero.realizarMovimiento(columna, fila, jugador):  # Nota: x,y vs fila,columna
                    self.movimientos += 1
                    self.jugadorActual = "O" if jugador == "X" else "X"

            return True
        except Exception as e:
            print(f"Error al cargar configuración con minidom: {e}")
            return False
    
    def cargarConfiguracionElemenTree(self, archivo):
        """Carga la configuración usando ElementTree"""
        try:
            tree = ET.parse(archivo)
            root = tree.getroot()
            
            # Obtener configuración
            config = root.find("configuracion")
            filas = int(config.find("filas").text)
            columnas = int(config.find("columnas").text)
            self.jugadorActual = config.find("jugador_inicial").text
            
            # Crear tablero con nuestras estructuras
            self.tablero = TableroTotito(filas, columnas)
            self.movimientos = 0
            
            # Cargar movimientos iniciales
            movimientos = root.find("movimientos")
            for mov in movimientos.findall("movimiento"):
                fila = int(mov.get("fila"))
                columna = int(mov.get("columna"))
                jugador = mov.get("jugador")
                if self.tablero.realizarMovimiento(columna, fila, jugador):  # Nota: x,y vs fila,columna
                    self.movimientos += 1
                    self.jugadorActual = "O" if jugador == "X" else "X"

            return True
        except Exception as e:
            print(f"Error al cargar configuración con ElementTree: {e}")
            return False
    
    def jugar(self):
        """Método principal para jugar el juego"""
        if self.tablero is None:
            print("Error: No se ha cargado la configuración del juego.")
            return
        
        print("¡Que comience el juego!")
        print(f"Tablero de {self.tablero.filas}x{self.tablero.columnas}")
        print("Ingresa coordenadas (fila columna), ej: 0 1")
        
        while True:
            self.tablero.imprimirTablero()
            
            try:
                entrada = input(f"Jugador {self.jugadorActual}, ingresa coordenadas (fila columna): ").split()
                if len(entrada) != 2:
                    print("¡Debes ingresar exactamente dos números!")
                    continue
                
                fila = int(entrada[0])
                columna = int(entrada[1])
                

                if not self.tablero.realizarMovimiento(columna, fila, self.jugadorActual):  # Nota: x,y vs fila,columna
                    print("¡Movimiento inválido! Intenta de nuevo.")
                    continue
                
                self.movimientos += 1
                
                print("jugadorActual",self.jugadorActual)
                # Verificar si hay ganador
                if self.tablero.verificarGanador(self.jugadorActual):
                    self.tablero.imprimirTablero()
                    print(f"¡Jugador {self.jugadorActual} ha ganado!")
                    return self.jugadorActual
                
                # Verificar empate
                if self.tablero.tableroLleno():
                    self.tablero.imprimirTablero()
                    print("¡Empate!")
                    return None
                
                # Cambiar jugador
                self.jugadorActual = "O" if self.jugadorActual == "X" else "X"
                
            except ValueError:
                print("¡Input inválido! Ingresa dos números separados por espacio.")
            except Exception as e:
                print(f"Error inesperado: {e}")
    
    def generarResultadoMinidom(self, archivo, ganador):
        """Genera el archivo XML de resultado usando minidom"""
        try:
            doc = minidom.Document()
            
            # Crear elemento raíz
            totito = doc.createElement("totito")
            doc.appendChild(totito)
            
            # Sección de resultado
            resultado = doc.createElement("resultado")
            totito.appendChild(resultado)
            
            if ganador:
                ganadorElem = doc.createElement("ganador")
                ganadorElem.appendChild(doc.createTextNode(ganador))
                resultado.appendChild(ganadorElem)
                
                perdedorElem = doc.createElement("perdedor")
                perdedorElem.appendChild(doc.createTextNode("O" if ganador == "X" else "X"))
                resultado.appendChild(perdedorElem)
            else:
                empateElem = doc.createElement("empate")
                empateElem.appendChild(doc.createTextNode("true"))
                resultado.appendChild(empateElem)
            
            # Sección de tablero
            tableroElem = doc.createElement("tablero")
            tableroElem.setAttribute("filas", str(self.tablero.filas))
            tableroElem.setAttribute("columnas", str(self.tablero.columnas))
            totito.appendChild(tableroElem)
            
            # Recorrer el tablero usando nuestras estructuras
            encabezado = self.tablero.matriz.primero
            while encabezado != None:
                filaElem = doc.createElement("fila")
                filaElem.setAttribute("id", str(encabezado.dato.posY))
                tableroElem.appendChild(filaElem)

                colElem = doc.createElement("columna")
                colElem.setAttribute("id", str(encabezado.dato.posX))
                colElem.appendChild(doc.createTextNode(encabezado.dato.jugador))
                filaElem.appendChild(colElem)

                celda = encabezado.fila.primero
                while celda != None:
                    columnaElem = doc.createElement("columna")
                    columnaElem.setAttribute("id", str(celda.dato.posX))
                    columnaElem.appendChild(doc.createTextNode(celda.dato.jugador))
                    
                    filaElem.appendChild(columnaElem)

                    celda = celda.siguiente
                
                
                encabezado = encabezado.siguiente

        
            
            # Escribir archivo
            with open(archivo, "w") as f:
                f.write(doc.toprettyxml(indent="  "))
            
            print(f"Resultado guardado en {archivo}")
            return True
        except Exception as e:
            print(f"Error al generar XML con minidom: {e}")
            return False
    
    def generarResultadoElementTree(self, archivo, ganador):
        """Genera el archivo XML de resultado usando ElementTree"""
        try:
            # Crear elemento raíz
            totito = ET.Element("totito")
            
            # Sección de resultado
            resultado = ET.SubElement(totito, "resultado")
            
            if ganador:
                ganadorElem = ET.SubElement(resultado, "ganador")
                ganadorElem.text = ganador
                
                perdedorElem = ET.SubElement(resultado, "perdedor")
                perdedorElem.text = "O" if ganador == "X" else "X"
            else:
                empateElem = ET.SubElement(resultado, "empate")
                empateElem.text = "true"
            
            # Sección de tablero
            tableroElem = ET.SubElement(totito, "tablero")
            tableroElem.set("filas", str(self.tablero.filas))
            tableroElem.set("columnas", str(self.tablero.columnas))
            
            # Recorrer el tablero usando nuestras estructuras
            encabezado = self.tablero.matriz.primero
            while encabezado != None:
                filaElem = ET.SubElement(tableroElem, "fila")
                filaElem.set("id", str(encabezado.dato.posY))

                colElem = ET.SubElement(filaElem, "columna")
                colElem.set("id", str(encabezado.dato.posX))
                colElem.text = encabezado.dato.jugador

                celda = encabezado.fila.primero

                while celda != None:
                    columnaElem = ET.SubElement(filaElem, "columna")
                    columnaElem.set("id", str(celda.dato.posX))
                    columnaElem.text = celda.dato.jugador
                    celda = celda.siguiente
                
                encabezado = encabezado.siguiente

            
            # Crear árbol y escribir archivo
            tree = ET.ElementTree(totito)
            ET.indent(tree, space="  ")  # Formatear con indentación
            tree.write(archivo, encoding="utf-8", xml_declaration=True)
            
            print(f"Resultado guardado en {archivo}")
            return True
        except Exception as e:
            print(f"Error al generar XML con ElementTree: {e}")
            return False