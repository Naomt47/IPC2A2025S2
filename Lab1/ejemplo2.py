
"""
Juego de Totito

Implementa el clásico juego "Totito" para dos jugadores en consola.

- El tablero es una cuadrícula de 3x3.
- Los jugadores (X y O) alternan turnos para marcar casillas vacías.
- El juego termina cuando un jugador forma una línea horizontal, vertical o diagonal, o si no hay más movimientos posibles (empate).
"""
def imprimirTablero(tablero):
    """Imprime el tablero """
    print("\n  0 1 2")  # Encabezado de columnas
    for i in range(3):  # Iterar sobre filas
        print(i, end=" ") # Imprimir número de fila
        for j in range(3):  # Iterar sobre columnas
            print(tablero[i][j], end="")
            if j < 2:  # Añadir separador "|" entre columnas
                print("|", end="")
        print()
        if i < 2:  # Añadir línea horizontal entre filas
            print("  -----")

# 7. Verificar si hay un ganador 
# -- crear una funcion que verifique si el jugador actual ganó 
# Un jugador gana cuando: 
# forma una línea horizontal, vertical o diagonal. 

def verificarGanador(tablero, jugador):
    """Verifica si el jugador actual ganó"""
    # Revisar filas
    for fila in range(3):
        ganador = True # Inicializamos la bandera como "True" (asumimos que gana)
        for columna in range(3):
            if tablero[fila][columna] != jugador:
                ganador = False
                break
    
        if ganador: # if ganador == True:
            return True
        
    # Revisar columnas
    for columna in range(3):
        ganador = True
        for fila in range(3):
            if tablero[fila][columna] != jugador:
                ganador = False
                break
        if ganador:
            return True
    
    # Revisar diagonales
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True

    return False



# comentario una linea

#1. Definir el tablero inicial
tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

"""tablero = [
    ["X", "X", "X"],
    ["X", "X", "X"],
    ["X", "X", "X"]
]
"""

def jugarTotito():
    # 2. Jugador X inicia siempre -> el primer turno es para X
    jugador_actual = "X"
    movimientos = 0

    print("¡Que comience el juego!")
    print("Ingresa coordenadas (fila columna), ej: 0 1")

    while True:
        #4.1 funcion para visualizar el estado del tablero (que espacios estan ocupados, etc.)
        imprimirTablero(tablero)


        #4.2 Manejar los posibles errores del usuario 
        #   (ej: si el usuario ingresa una letra en lugar de un numero)
        try:
            #4.solicitar corrdenadas 
            entrada = input("Coordenadas (fila columna): ").split() #["1", "0"]
            fila = int(entrada[0])
            columna = int(entrada[1])

            # validar que las coordenadas esten dentro del rango del tablero
            if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                print("¡Coordenadas fuera de rango! Usa números entre 0 y 2.")
            
            # 5. Verificar coordenadas después de cada movimiento
            if tablero[fila][columna] != " ":
                print("¡Casilla ocupada! Intenta otra.")
            
        except (ValueError, IndexError):
            print("¡Input inválido! Ingresa dos números separados por espacio.")

        # 6. Actualizar el tablero
        tablero[fila][columna] = jugador_actual
        movimientos += 1

        if verificarGanador(tablero, jugador_actual):
            imprimirTablero(tablero)
            print(f"¡Jugador {jugador_actual} ha ganado!")
            break
        elif movimientos == 9:
            imprimirTablero(tablero)
            print("¡Empate!")
            break

        if jugador_actual == "X":
            jugador_actual = "O"
        else: 
            jugador_actual = "X"



jugarTotito()


