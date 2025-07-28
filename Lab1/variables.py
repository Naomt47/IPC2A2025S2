"""
1.3.1. Variables, expresiones y sentencias
"""

# En Python, no es necesario declarar el tipo de una variable.
edad = 25 
nombre = "Juan Pérez"
altura = 1.75
es_estudiante = True

# Operaciones aritméticas (similares a Java)
suma = 3 + 5       # 8
resta = 10 - 2      # 8
multiplicacion = 4 * 2  # 8
division = 16 / 2    # 8.0 (en Python 3, la división siempre retorna float)
division_entera = 13 // 2  # 6
modulo = 15 % 4     # 3 (resto de la división)

# impresiones:
print(suma)
print(resta)
print(multiplicacion)
print(division)
print(division_entera)
print(modulo)

# Entrada de usuario
# Java: Scanner scanner = new Scanner(System.in); String entrada = scanner.nextLine();
entrada_usuario = input("Ingresa tu edad: ")  # Retorna un string
edad_usuario = int(entrada_usuario)  # Conversión a entero
print(type(edad_usuario))