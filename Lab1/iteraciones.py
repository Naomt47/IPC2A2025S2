"""
1.3.4. Iteración 
"""

for i in range(5):  # range(5) = 0, 1, 2, 3, 4
    print(i)

# Listas:
listaEjemplo = [1,2,3]
listaEjemplo2 = [1, "a", True]

frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# Bucle while
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1