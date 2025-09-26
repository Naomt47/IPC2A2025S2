from flask import Flask, render_template,  request, send_file
from ListaDoble import ListaDoble
import os

app = Flask(__name__)
lista_doble = ListaDoble()


@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = ""
    if request.method == 'POST':
        if 'xml_file' in request.files and 'parser' in request.form:
            xml_file = request.files['xml_file']
            parser = request.form['parser']

            if xml_file.filename.endswith('.xml'):
                # Guardar el archivo temporalmente
                xml_path = os.path.join('static', xml_file.filename)
                xml_file.save(xml_path)

                # Cargar datos según el parser seleccionado
                
                try:
                    lista_doble.cargarXML(xml_path, parser)
                    lista_doble.graficar() #Graficar la gráfica
                    mensaje = "Archivo XML cargado exitosamente"
                except Exception as e:
                    mensaje = f"Error al cargar el XML: {str(e)}"
                finally:
                    if os.path.exists(xml_path):
                        os.remove(xml_path)
            
            else:
                mensaje = "Por favor, sube una archivo xml"

    return render_template('index.html', lista=lista_doble, mensaje=mensaje)

@app.route('/visualizarPDF')
def visualizarPDF():
    return render_template("visualizarPDF.html")

@app.route('/enunciado')
def servirPDF():
    return send_file('static/[IPC2]Proyecto2_202502_v2.pdf', as_attachment=False)


if __name__ == '__main__':
    app.run(debug=True)