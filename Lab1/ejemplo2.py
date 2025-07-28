
"""
Juego de Totito

Implementa el clásico juego "Totito" para dos jugadores en consola.

- El tablero es una cuadrícula de 3x3.
- Los jugadores (X y O) alternan turnos para marcar casillas vacías.
- El juego termina cuando un jugador forma una línea horizontal, vertical o diagonal, o si no hay más movimientos posibles (empate).
"""


# comentario una linea

#1. Definir el tablero inicial
"""tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]"""

tablero = [
    ["X", "X", "X"],
    ["X", "X", "X"],
    ["X", "X", "X"]
]


# 2. Jugador X inicia siempre -> el primer turno es para X
jugador_actual = "X"
movimientos = 0

def imprimirTablero(tablero):
    """Imprime el tablero """
    print("\n  0 1 2")  # Encabezado de columnas
    for i in range(3):  # Iterar sobre filas
        print(i, end="")
        for j in range(3):  # Iterar sobre columnas
            print(tablero[i][j], end="")
            if j < 2:  # Añadir separador "|" entre columnas
                print("|", end="")
        print()
        if i < 2:  # Añadir línea horizontal entre filas
            print("  -----")


#3.1 funcion para visualizar el estado del tablero (que espacios estan ocupados, etc.)
imprimirTablero(tablero)


#3.2 Manejar los posibles errores del usuario (ej: si el usuario ingre una letra en lugar de un numero)
try:
    entrada = input("Coordenadas (fila columna): ").split()
    fila = int(entrada[0])
    columna = int(entrada[1])

    # 4. Verificar coordenadas después de cada movimiento

    # validar que las coordenadas esten dentro del rango del tablero
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("¡Coordenadas fuera de rango! Usa números entre 0 y 2.")
    
    if tablero[fila][columna] != " ":
        print("¡Casilla ocupada! Intenta otra.")
    
except (ValueError, IndexError):
    print("¡Input inválido! Ingresa dos números separados por espacio.")



