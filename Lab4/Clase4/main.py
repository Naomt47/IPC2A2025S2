import xml.etree.ElementTree as ET # Importar librería ElementTree
from xml.dom import minidom # Importar librería minidom

def Menu():
    print(' ------------- Menu Principal -------------')
    print('1. Leer archivo XML (ElementTree)')
    print('2. Leer archivo XML (minidom)')
    print('3. Salir')
    print(' ------------------------------------------')

    opc = int(input('Ingrese una opción: '))
    return opc

def LeerArchivoET(rutaArchivo):
    tree = ET.parse(rutaArchivo) #Parsear el archivo XML
    root = tree.getroot() # Obtenemos la raíz, en este caso <listado>

    # Revisar cuál es la raíz del archivo XML:
    # print(root.tag)

    for banco_elem in root.findall('Banco'): #iterar
        #print(type(banco_elem), banco_elem)
        # get:
        #   - Se usa para extraer el valor de un atributo definido dentro de la etiqueta XML.

        nombreBanco = banco_elem.get('nombre') # Obtener el atributo nombre
        direccionBanco = banco_elem.get('direccion') # Obtener el atributo direccion
        
        # Se usa para buscar etiquetas hijas dentro del elemento actual.
        # Retorna el primer elemento que coincida con el nombre buscado.
        # Para obtener su texto, se usa .text.
        ant = int(banco_elem.find('Antiguedad').text) # Obtener el texto de la etiqueta Antiguedad
        sucursales = int(banco_elem.find('sucursales').text)
        
        
        print('\n BANCO: ',nombreBanco, direccionBanco, ant, sucursales )


        for cliente_elem in banco_elem.find('Clientes').findall('Cliente'):
            nombreCliente = cliente_elem.find('Nombre').text
            cuiCliente = int(cliente_elem.find('CUI').text)
            saldoCliente = float(cliente_elem.find('Saldo').text)
            edadCliente = int(cliente_elem.find('edad').text)


            print("\t CLIENTE: ", nombreCliente, cuiCliente, saldoCliente, edadCliente )


    print('Datos leídos con éxito con ElementTree')


def LeerArchivoMD(rutaArchivo):
    doc = minidom.parse(rutaArchivo) # Parsear el archivo XML
    root = doc.documentElement # Obtener la raíz del archivo XML

    bancos = root.getElementsByTagName('Banco') # Obtener todos los nodos Banco
    for banco in bancos:
        nombreBanco = banco.getAttribute('nombre') #Obtiene el valor de un atributo del elemento actual.
        direccionBanco = banco.getAttribute('direccion') 
        # getElementsByTagName -> Este método siempre retorna una NodeList (lista de nodos), incluso si hay solo un elemento.
        #   - Por eso necesitas [0] para acceder al primer elemento de la lista.

        # getAttribute() NO SE USA para elementos anidados
        #   - solo funciona con atributos dentro de la etiqueta, no con elementos hijos.

        # el texto no es una propiedad directa del elemento, sino un nodo hijo de tipo texto.
            #.firstChild -> Obtiene el primer nodo hijo del elemento (Ej: el nodo de texto con "26").
            #.data -> Extrae el contenido del nodo de texto (Ej: la cadena "26").
        ant = int(banco.getElementsByTagName('Antiguedad')[0].firstChild.data) 
        
        sucursales = int(banco.getElementsByTagName('sucursales')[0].firstChild.data)

        print('\n BANCO: ',nombreBanco, direccionBanco, ant, sucursales )


        clientes = banco.getElementsByTagName('Cliente')
        for cliente in clientes:
            nombreCliente = cliente.getElementsByTagName('Nombre')[0].firstChild.data
            cuiCliente = int(cliente.getElementsByTagName('CUI')[0].firstChild.data)
            saldoCliente = float(cliente.getElementsByTagName('Saldo')[0].firstChild.data)
            edadCliente = int(cliente.getElementsByTagName('edad')[0].firstChild.data)

            print("\t CLIENTE: ", nombreCliente, cuiCliente, saldoCliente, edadCliente )


    print('Datos leídos con éxito con minidom')



if __name__ == '__main__':
    opc = 0
    rutaArchivo = input("Ingrese la ruta del archivo: ")
    while opc != 3:
        opc = Menu()

        if opc == 1:
            print('')
            LeerArchivoET(rutaArchivo)
            
        elif opc == 2:
            print('')
            LeerArchivoMD(rutaArchivo)

        elif opc == 3:
            print('Adios')
            break
        else:
            print('Opción no válida')
            continue
        print('')    