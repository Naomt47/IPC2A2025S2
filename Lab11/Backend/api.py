from flask import Flask, jsonify, Response, request
# Importamos ElementTree para parsear XML en la ruta que recibe datos en este formato
from xml.etree import ElementTree as ET
# Importamos CORS para permitir solicitudes desde otros dominios (cross-origin), útil para frontend en otro servidor
from flask_cors import CORS

# Creamos la instancia de la aplicación Flask
api = Flask(__name__)

# Habilitamos CORS para permitir solicitudes desde otros orígenes (ej. un frontend en localhost:3000)
cors = CORS(api)

usuarios = []

@api.route("/")
def root():
    # Devuelve un mensaje simple en texto plano
    # En una API real, podrías devolver un JSON con información sobre la API
    return "Si firula Wujuu!!!"

# === PARÁMETROS EN LA URL ===
# Los parámetros en la URL pueden enviarse de dos formas:
# 1. **Path Parameters**: Parte de la URL, definidos en la ruta (ej. /usuario/saludar/202103095/Angely)
#    - Cuándo usar: Para identificar recursos específicos (ej. un usuario por ID) o datos requeridos.
#    - Ventajas: Claros, fáciles de leer, ideales para recursos REST (ej. /users/123).
#    - Desventajas: No son flexibles para datos opcionales o múltiples parámetros.
# 2. **Query Parameters**: Después de un "?" en la URL (ej. /usuario/saludar2?carnet=202103095&nombre=Angely)
#    - Cuándo usar: Para datos opcionales, filtros o búsquedas (ej. paginación, filtros).
#    - Ventajas: Flexibles, permiten múltiples parámetros, no modifican la estructura de la URL.
#    - Desventajas: Menos legible para recursos específicos, limitado para datos complejos.

# Ruta con Path Parameters
@api.route("/usuario/saludar/<int:carnet>/<string:nombre>", methods=['GET'])
def saludar(carnet, nombre):
    # Creamos un elemento XML raíz
    root = ET.Element("respuesta")
    # Añadimos subelementos para mensaje y status
    mensaje = ET.SubElement(root, "mensaje")
    mensaje.text = f'Hola {nombre} carnet {carnet}'
    status = ET.SubElement(root, "status")
    status.text = "200"

    # Convertimos el árbol XML a una cadena
    resXML = ET.tostring(root, encoding='unicode', method='xml')

    # Devolvemos la respuesta con Response, especificando Content-Type como application/xml
    return Response(resXML, mimetype='application/xml', status=200)


# Ruta con Query Parameters
@api.route('/usuario/saludar2', methods=['GET'])
def saludar2():
    id = request.args.get('carnet', type=int)
    nombre = request.args.get('nombre', type=str)

    # Devolvemos un JSON similar al ejemplo anterior
    return jsonify({
        'mensaje': f'Hola {nombre} carnet {id}',
    }), 200



# === PARÁMETROS EN EL BODY ===
@api.route('/usuario/add', methods=['POST'])
def agregarJson():
    data = request.get_json()
    nombre = data['nombre']
    carnet = data['carnet']

    # Creamos un nuevo usuario con un ID incremental (basado en la longitud de la lista)
    nuevoUsuario = {'id': len(usuarios) + 1, 'nombre': nombre, 'carnet': carnet}
    # Agregamos el usuario a la lista global (simula almacenamiento en una base de datos)
    usuarios.append(nuevoUsuario)

    # Devolvemos un JSON con un mensaje, el usuario creado y un código de estado 201 (Creado)
    return jsonify({
        'mensaje': 'Usuario creado exitosamente',
        'usuario': nuevoUsuario,
    }), 201

# Ruta que recibe XML en el body
# Ejemplo de solicitud POST con body XML:
""" 
<usuario>
     <nombre>Angely</nombre>
     <carnet>202103095</carnet>
</usuario>
"""
@api.route('/usuario/add2', methods=['POST'])
def agregarXML():
    xml = request.data.decode('utf-8')

    # Parseamos el XML usando ElementTree
    root = ET.fromstring(xml)
    # Extraemos los valores de las etiquetas <nombre> y <carnet>
    nombre = root.find('nombre').text
    carnet = root.find('carnet').text
    
    # Creamos un nuevo usuario igual que en la ruta JSON
    nuevoUsuario = {'id': len(usuarios) + 1, 'nombre': nombre, 'carnet': carnet}
    usuarios.append(nuevoUsuario)
    print(nuevoUsuario)  # Depuración: mostramos el usuario creado

    # Devolvemos un JSON con el resultado (aunque la entrada es XML, la respuesta es JSON)
    return jsonify({
        'mensaje': 'Usuario creado exitosamente',
        'usuario': nuevoUsuario
    }), 201









# Punto de entrada del programa
if __name__ == '__main__':
    # Inicia el servidor Flask
    # debug=True habilita el modo de depuración
    # Por defecto, usa puerto 5000 y host 'localhost'
    api.run(debug=True)