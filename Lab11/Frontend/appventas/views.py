from django.shortcuts import render
import requests
from .forms import FileForm, InputTextAreaForm #importar los forms de forms.py

endpoint = 'http://localhost:4000/'
# Create your views here.

#Esta es una vista de ejemplo, pero puedes agregar las que necesites
def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def carga(request):
    return render(request, 'carga.html')

#los contextos son las expresiones que se muestran en los templates
contexto = {
    'contenido_archivo':None,
    'binario_xml':None,
    'mensaje_error': None,
    'mensaje_exito': None,
    'salida_procesada': None
}

def cargarXML(request):
    try:
        if request.method == 'POST':
            #obtenemos el formulario
            form = FileForm(request.POST, request.FILES)
            #verificamos si es valido
            if form.is_valid():
                #obtenemos el archivo
                archivo = request.FILES['file'] #file es el label que estamos obteniendo (el nombre que se coloco en id,for,name y en el form)
                #leemos el archivo
                contenido = archivo.read()
                #decodificamos el archivo a utf-8
                contenido_xml = contenido.decode('utf-8')
                #guardamos el contenido en el contexto
                contexto['contenido_archivo'] = contenido_xml
                contexto['binario_xml'] = contenido
                #enviamos el archivo al servidor
                contexto['mensaje_exito'] = 'Archivo cargado al sistema'
                return render(request, 'carga.html', contexto) #le mando el contexto
    except:
        contexto['mensaje_error'] = 'Error al cargar el archivo'
        return render(request, 'carga.html', contexto)

def cerrarMensajesCargarXML(request):
    contexto['mensaje_error'] = None
    contexto['mensaje_exito'] = None
    return render(request, 'carga.html', contexto)


#request sin s es el de django    
def procesarXML(request):
    try:
        if request.method == 'POST':
            #obtenemos el archivo
            archivo = contexto['binario_xml']
            if archivo is None:
                return render(request, 'carga.html')
            #enviamos el archivo al servidor 
            ##request con s es para conectarnos con el backend
            response = requests.post(endpoint + 'venta/cargar', data=archivo) #/venta/cargar
            #obtenemos la respuesta en formato json
            respuesta = response.json()
            #guardamos la respuesta en el contexto
            print(respuesta['mensaje'])
            #limpiamos el contexto
            contexto['contenido_archivo'] = None
            contexto['binario_xml'] = None
            contexto['mensaje_exito'] = 'Ventas procesadas correctamente en el sistema'
            return render(request, 'carga.html', contexto)
    except:
        contexto['mensaje_error'] = 'Error al procesar el archivo en el servidor'
        return render(request, 'carga.html')
    
def verTablaVentas(request):
    ctx = {
        'ventas': None
    }
    response = requests.get(endpoint + 'venta/ventas')
    data = response.json()
    if response.status_code == 200:
        ctx['ventas'] = data
    return render(request, 'ventas.html', ctx)


def verVentasMensuales(request):
    return render(request, 'ventaspormes.html')

def verPdf(request):
    return render(request, 'verpdf.html')