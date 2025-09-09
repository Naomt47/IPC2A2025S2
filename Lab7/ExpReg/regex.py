import re 

#Buscar una palabra en una cadena


patron = r"hola"
cadena = "hola mundo"

resultado = re.search(patron, cadena)
if resultado:
    print("Se encontro el patron")
else:
    print("No se encontro el patron")

#^(alt + 94)  Buscar si una cadena empieza con una palabra especifica 
patron_inicio = r"^hola"
resultado = re.search(patron_inicio, cadena)
if resultado:
    print("La cadena empieza con hola")
else:
    print("La cadena No empieza con hola")

#$ Busca si una cadena termina con una palabra específica 
patron_final = r"mundo$"
resultado = re.search(patron_final, cadena)
if resultado:
    print("La cadena termina con mundo")
else:
    print("La cadena No termina con mundo")


#\ barra invertida 
#    1. Secuencias especiales que empiezan por '\'



#Encontrar todas las palabras en una cadena
patron = r"\b\w+\b"
cadena = "El sol brilla y el viento sopla"

#\b : un limite de palabra (marca el principio o el final de una palabra)
#\w+ : acepta letras, numeros o guiones bajos

resultados = re.findall(patron, cadena)
print("Palabras encontradas: ", resultados)


#Dividir una cadena en  palabras
patron = r"\s+"
cadena = "Estas es una cadena con    espacios en blanco"
#\s 
partes = re.split(patron, cadena)
print("Partes de la cadena:", partes)


#Sustituir todas las ocurrencias en una palabra por otra
patron = r"mundo"
cadena = "Hola mundo, mundo, mundo!"
nueva_cadena = re.sub(patron, "Python", cadena)
print("Cadena despues de la sustitucion: ", nueva_cadena)


#----------------- REPETICIONES
#+ comprueba si el caracter precende aparece una o más veces a partir de esa posición
#* comprueba si el caracter precende aparece cero más veces a partir de esa posición
#? comprueba si el caracter precende aparece cero o una vez a partir de esa posición

#Captura el nombre y el dominio de un correo electronico
patron = r"(\w+)@(\w+\.\w+)" 
#Caso 3: \ puede utilizarse delante de todos los metacaracteres para eliminar su significado especial \.
cadena = "correo@example.com"

resultado = re.search(patron, cadena)
if resultado:
    nombre = resultado.group(1)
    dominio = resultado.group(2)

    print(f"Nombre: {nombre}, Dominio: {dominio}")

else: 
    print("No se encontró el patrón")

#Buscar una palabra independientemente de mayúsculas o minúsculas 
patron = r"python"
cadena = "Me encanta Python y python"
resultados = re.findall(patron, cadena, re.IGNORECASE)
print("Coincidencias encontradas: ", resultados)

#Validar un número de teléfono (formato: XXX-XXX-XXXX)
patron = r"^\d{3}-\d{3}-\d{4}"
telefono = "123-456-7890"
if re.match(patron, telefono):
    print("Número de teléfono válido")
else: 
    print("Número de teléfono inválido")


#Compilar un patrón y usarlo varias veces 
patron_compilado = re.compile( r"^\d{3}-\d{3}-\d{4}")
telefonos = ["123-456-7890", "987-654-3210", "1234567890"]

for telefono in telefonos:
    if patron_compilado.match(telefono):
        print(f"{telefono} es valido")
    else: 
        print(f"{telefono} no es valido")