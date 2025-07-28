def suma(a, b):
    return a + b

# Parámetros opcionales (no existe en Java)
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}")

saludar("Ana")           # "Hola, Ana"
saludar("Pedro", "Que onda") # "Hola, Pedro"
