"""
1.3.2. Ejecución condicional
"""


a = -1 # entero
b = 3 # entero
edad = 23

if a == 1:
    print('Si, "a" si posee el valor de 1.')
else:
    print("No, 'a' no posee el valor de 1.")

# Operadores lógicos:
# Python: and, or, not ------------------ Java: &&, ||, !

if a == 1 and b == 2:
    print("Se cumple con las condiciones")
elif a == 2 or int(edad)== 23:
    print("Se cumple alguna de las condiciones")
elif not a == 1:
    print("Se cumple con que 'a' NO es 1")
else:
    print("Ninguna de las condiciones se cumple")


# Operadores de comparación:
# ==, !=, <, >, <=, >=
# igual que, no es igual, menor qué, mayor qué, menor igual qué, mayor igual qué:

# Java: if (edad >= 18) { System.out.println("Mayor de edad"); }
if edad >= 18:
    print("Mayor de edad")  # Sangría obligatoria (no hay {})
else:
    print("Menor de edad")