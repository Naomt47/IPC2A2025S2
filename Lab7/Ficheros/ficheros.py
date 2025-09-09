"""
Ejercicio: Procesar y Clasificar Contenido de un Archivo de Texto
Descripción: En este ejercicio, se escribirá un script en Python que:

    Abre un archivo de texto llamado texto_entrada.txt.
    Lee el contenido línea por línea.
    Realiza un análisis y clasificación del contenido, incluyendo:
        Contar cuántas líneas comienzan con una vocal y cuántas comienzan con una consonante.
        Contar el número de líneas que contienen números.
        Identificar si hay líneas completamente en mayúsculas.
    Escribe un resumen detallado en un nuevo archivo llamado reporte_analisis.txt.
"""

def comienzaConVocal(linea):
    return linea[0].lower() in "aeiou"

#Abre un archivo de texto llamado texto_entrada.txt.
with open("texto_entrada.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

lineasConVocal = 0
lineasConConsonante = 0
lineasConNumeros = 0
lineasEnMayus = []
#Lee el contenido línea por línea.
for linea in lineas:
    lineaStrip = linea.strip()
    print(lineaStrip) 
    if lineaStrip[0].isalpha(): #a-z
        if comienzaConVocal(lineaStrip):
            lineasConVocal += 1
        else:
            lineasConConsonante += 1

    
    if any(caracter.isdigit() for caracter in lineaStrip):
        lineasConNumeros += 1

    
    if lineaStrip.isupper():
        lineasEnMayus.append(lineaStrip)

    print(f"{lineasConNumeros}")
    print(f"{lineasConNumeros}")


with open("reporteAnalisis.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Reporte Analisis de Archivo Texto_Entrada.txt \n")
    archivo.write(f"Numero de lineas que comienzan con una vocalf: {lineasConVocal} \n")
    archivo.write(f"Numero de lineas que comienzan con una consonante: {lineasConConsonante} \n")
    archivo.write(f"Numero de lineas que contienen numeros : {lineasConNumeros} \n")
    archivo.write(f"Numero de lineas que en mayusculas: {lineasConVocal} \n")
    for linea in lineasEnMayus:
        archivo.write(f"- {linea} \n")

print("listo")