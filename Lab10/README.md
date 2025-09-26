# Desarrollo Web con Flask 

**Requisitos**:
- Python 3 instalado.
- Instalar Flask: `pip install flask`
- Un editor de texto (VS Code, IDLE) y un navegador.

---

## 1. ¿Es Flask una Biblioteca o un Framework?

Flask es un **microframework web**, no solo una biblioteca. Aquí la diferencia:

- **Biblioteca**: Conjunto de funciones que usas en tu código (ej. `math` para cálculos). Tú controlas el flujo del programa.
- **Framework**: Estructura que define cómo organizar tu aplicación, con herramientas para tareas comunes (como manejar rutas HTTP). El framework guía el flujo, y tú completas los detalles.
- **Flask como microframework**: Es un framework porque proporciona una estructura para aplicaciones web (rutas, plantillas, solicitudes HTTP). Es "micro" porque es ligero, sin componentes complejos como bases de datos integradas (a diferencia de Django), pero es extensible con bibliotecas adicionales.

**Por qué usarlo**: Flask es ideal para principiantes por su simplicidad y flexibilidad. Nos permite crear un frontend con HTML dinámico rápidamente, perfecto para el juego de totito.

---

## 2. Introducción a Flask

**Flask** es un microframework web de Python que permite:
- **Manejar rutas**: Asociar URLs (ej. `/jugar`) a funciones Python.
- **Renderizar plantillas**: Generar HTML dinámico con datos de Python usando Jinja2.
- **Procesar solicitudes**: Manejar formularios y entradas de usuarios.
- **Servir contenido**: Mostrar páginas web en un navegador.

### 2.1. Aspectos Clave de Flask

- **Ligero y modular**: Solo incluye lo esencial, permitiendo agregar funcionalidades según necesidad (ej. no incluye base de datos por defecto).
- **Jinja2 integrado**: Motor de plantillas para generar HTML dinámico.
- **Soporte para HTTP**: Maneja métodos GET (obtener páginas) y POST (enviar datos de formularios).
- **Modo debug**: Con `app.run(debug=True)`, muestra errores en el navegador, ideal para desarrollo.
- **Estructura flexible**: Puedes organizar tu proyecto como quieras, pero Flask espera ciertas convenciones (como la carpeta `templates`).

### 2.2. Sintaxis Básica de Flask

1. **Crear la aplicación**:
```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Inicializa la app con el nombre del módulo
```

- `Flask(__name__)`: Crea la aplicación. `__name__` ayuda a Flask a encontrar las carpetas `templates` y `static`.
- Módulos comunes:
  - `render_template`: Renderiza archivos HTML.
  - `request`: Accede a datos de formularios o URLs.
  - `redirect` y `url_for`: Redirigen a otras rutas.

2. **Definir rutas**:
```python
@app.route('/')
def index():
    return render_template('index.html', mensaje='Bienvenido')
```

- `@app.route('/')`: Vincula la URL `/` a la función `index()`.
- `render_template('index.html', mensaje='Bienvenido')`: Muestra `index.html` con una variable `mensaje`.

3. **Manejar formularios (POST)**:
```python
@app.route('/submit', methods=['POST'])
def submit():
    dato = request.form['nombre']  # Obtiene el campo 'nombre' del formulario
    return render_template('resultado.html', dato=dato)
```

- `methods=['POST']`: Permite solicitudes POST.
- `request.form`: Diccionario con datos del formulario.

4. **Archivos estáticos** (CSS, JS):
```python
# Enlazar en HTML
<link rel="stylesheet" href="{{ url_for('static', filename='estilos.css') }}">
```

- `url_for('static', filename='...')`: Genera URLs para archivos en la carpeta `static`.

### 2.3. Estructura del Proyecto

Una aplicación Flask típica tiene esta estructura:

```
project/
├── app.py                # Código principal de Flask
├── templates/           # Archivos HTML (plantillas)
│   ├── index.html
│   └── juego.html
├── static/              # Archivos CSS, JS, imágenes
│   └── estilos.css
```

- **app.py**: Se inicializa la aplicación.
- **templates/**: Contiene archivos HTML renderizados por Jinja2.
- **static/**: Archivos estáticos como CSS.


### 2.4. Importancia de la Carpeta `templates`

La carpeta `templates` es **obligatoria** en Flask porque:
- **Convención de Flask**: Flask busca archivos HTML en una carpeta llamada exactamente `templates` en la raíz del proyecto. Si no existe o tiene otro nombre, Flask no los encuentra y lanza un error (`TemplateNotFound`).
- **Separación de lógica y presentación**: Las plantillas HTML separan el código Python (en `app.py`) de la interfaz de usuario, haciendo el código más organizado y mantenible.
- **Jinja2**: La carpeta `templates` es donde Jinja2 busca archivos para renderizar dinámicamente.

**Nota**: El nombre `templates` no se puede cambiar sin configurar Flask explícitamente.

---

## 3. ¿Por Qué Usamos Jinja2?

**Jinja2** es el motor de plantillas integrado en Flask, que permite generar HTML dinámico combinando código HTML con datos de Python. Es como un "generador de páginas" que inserta variables, bucles y condicionales en el HTML.

### 3.1. Razones para Usar Jinja2

- **Dinamismo**: Permite mostrar datos variables (ej. el tablero de totito) sin escribir HTML estático para cada caso.
- **Reutilización**: Puedes crear plantillas base y extenderlas (herencia de plantillas), aunque no lo usaremos aquí.
- **Seguridad**: Escapa automáticamente caracteres especiales (ej. `<` se convierte en `&lt;`) para prevenir ataques XSS.
- **Integración con Python**: Permite usar estructuras de datos (como listas enlazadas) directamente en HTML.


### 3.2. Sintaxis Detallada de Jinja2

Jinja2 usa tres tipos de delimitadores en HTML:
1. **Variables**: `{{ variable }}`
   - Inserta el valor de una variable Python.
   - Ejemplo: `<h1>Hola, {{ nombre }}!</h1>` muestra "Hola, Juan!" si `nombre='Juan'`.
   - **Filtros**: Modifican la salida, ej. `{{ nombre|upper }}` (convierte a mayúsculas), `{{ lista|length }}` (tamaño de la lista).
     - Filtros comunes: `upper`, `lower`, `trim`, `default('valor')`.

2. **Bloques de control**: `{% bloque %} ... {% endbloque %}`
   - Para bucles, condicionales y más.
   - **Bucles**:
     ```html
     <ul>
         {% for item in lista %}
             <li>{{ item }}</li>
         {% endfor %}
     </ul>
     ```
     - Recorre `lista` y genera un `<li>` por elemento.
   - **Condicionales**:
     ```html
     {% if condicion %}
         <p>Condición verdadera</p>
     {% else %}
         <p>Condición falsa</p>
     {% endif %}
     ```
     - Muestra contenido según una condición.
   - **Bloques extendidos** (no usado aquí):
     ```html
     {% extends 'base.html' %}
     {% block contenido %}...{% endblock %}
     ```

3. **Comentarios**: `{# comentario #}`
   - No se muestran en el HTML renderizado.
   - Ejemplo: `{# Esto no se ve en la página #}`

4. **Acceso a objetos**: `{{ objeto.atributo }}`
   - Ejemplo: `{{ celda.id }}` accede al atributo `id` de un objeto `Banco`.
   - Para listas enlazadas: `{% for celda in lista_enlazada %}{{ celda.id }}{% endfor %}`.

5. **Funciones de Jinja2**:
   - `{{ url_for('nombre_ruta') }}`: Genera URLs para rutas (ej. `/visualizarPDF`).
   - `{{ url_for('static', filename='estilos.css') }}`: Enlaza archivos estáticos.


---
