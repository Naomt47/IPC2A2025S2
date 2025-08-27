from ListaDeListas.ListaDoble import ListaDoble
from ListaDeListas.NodoCelda import Celda



class TableroTotito:
    def __init__(self, filas=3, columnas=3):
        self.filas = filas
        self.columnas = columnas
        self.matriz = ListaDoble()
        self.inicializarTablero()
        

    def inicializarTablero(self):
        #Método para inicializar el tablero con espacios vacíos
        for y in range(self.filas):
            encabezado = self.matriz.agregarUltimo(Celda(posicionX=0, posicionY=y))
            for x in range(1,self.columnas):
                encabezado.fila.agregarUltimo(Celda( posicionX=x, posicionY=y))

        print("se inicializó el tablero con éxito")


    def realizarMovimiento(self, x, y, jugador):
        """Intenta realizar un movimiento en el tablero"""
        if x < 0 or x >= self.columnas or y < 0 or y >= self.filas:
            return False  # Movimiento fuera de rango
        
        celda = self.matriz.ObtenerPorPosicion(x,y)
        if celda:
            #Verficar si la celda esta vacia
            if celda.dato.jugador != " ":
                return False
            else:
                celda.dato.jugador = jugador
                return True
        return False

    def verificarGanador(self, jugador):
        """Verifica si el jugador actual ganó"""
        # Verificar filas
        tempEncabezado = self.matriz.primero
        while tempEncabezado != None:
            ganador = True
            if tempEncabezado.dato.jugador == jugador:
                celda = tempEncabezado.fila.primero
                while celda != None:
                    if celda.dato.jugador != jugador:
                        ganador = False
                        break
                    celda = celda.siguiente
            else:
                ganador = False

            if ganador:
                print(f"Totito en fila {tempEncabezado.dato.posY}")
                return True
    
            tempEncabezado = tempEncabezado.siguiente


        
        # Verificar columnas
        for x in range(self.columnas):
            ganador = True
            for y in range(self.filas):
                celda = self.matriz.ObtenerPorPosicion(x,y)
                if celda is None or celda.dato.jugador != jugador:
                    ganador = False
                    break
            
            if ganador:
                print(f"Totito en columna {x}")
                return True

        
        # Verificar diagonal principal (solo si el tablero es cuadrado)
        if self.filas == self.columnas:
            ganador = True
            for i in range(self.filas):
                celda = self.matriz.ObtenerPorPosicion(i,i)
                if celda is None or celda.dato.jugador != jugador:
                    ganador = False
                    break
            
            if ganador:
                print(f"Totito en diagonal principal")
                return True
            
            # Verificar diagonal secundaria
            ganador = True
            for i in range(self.filas):
                celda = self.matriz.ObtenerPorPosicion(self.filas - 1 - i,i)
                if celda is None or celda.dato.jugador != jugador:
                    ganador = False
                    break


            if ganador:
                print(f"Totito en diagonal secundaria")
                return True
        
        return False


    def tableroLleno(self):

        tempEncabezado = self.matriz.primero
        while tempEncabezado != None:
            
            if tempEncabezado.dato.jugador == " ":
                return False
            
            celda = tempEncabezado.fila.primero
            while celda != None:
                if celda.dato.jugador == " ":
                    return False
                celda = celda.siguiente

            tempEncabezado = tempEncabezado.siguiente
        return True
    
    def imprimirTablero(self):
        """Imprime el tablero con coordenadas"""
        # Encabezado de columnas
        print("\n  ", end="")
        for x in range(self.columnas):
            print(" ", x, end=" ")
        print()
        self.matriz.imprimirMatriz()

    def graficarTablero(self):
        self.matriz.graficar()