# Guía de HTML5 y CSS

---

## 5. HTML5 y CSS

HTML5 (HyperText Markup Language versión 5) es el lenguaje estándar para crear la estructura de páginas web. Es un lenguaje de **marcado**, no de programación como Python, lo que significa que usa **etiquetas** (tags) para describir el contenido, en lugar de lógica o variables. CSS (Cascading Style Sheets) es un lenguaje de estilos que define cómo se ve ese contenido (colores, tamaños, layouts).

Juntos, HTML5 y CSS permiten crear sitios web responsivos (que se adaptan a móviles y desktops). HTML5 es la evolución de HTML4, con soporte para multimedia (videos, audio) y APIs modernas.

### 5.1. Introducción a HTML5 y CSS

- **HTML5**: Define la semántica (significado) de una página. Por ejemplo, `<h1>` indica un título principal, no solo texto grande. Es interpretado por navegadores como Chrome o Firefox.
- **CSS**: Controla la presentación. "Cascading" significa que los estilos se aplican en capas (de general a específico), y si hay conflictos, el más específico gana.
  
**Por qué aprenderlos**: Son la base del 90% de las webs. Sin HTML, no hay estructura; sin CSS, todo se ve plano y aburrido. Piensen en HTML como bloques de Lego y CSS como pintura y pegamento.

**Requisitos básicos**: Un editor de texto y un navegador. No necesitan instalar nada extra al inicio.

### 5.2. Estructura básica

Un documento HTML5 tiene una estructura fija, como un esqueleto. Siempre comienza con una declaración DOCTYPE y envuelve todo en `<html>`. Aquí va la sintaxis básica:

```html
<!DOCTYPE html>  <!-- Declara que es HTML5 -->
<html lang="es">  <!-- Etiqueta raíz, lang indica el idioma (español) -->
<head>
    <meta charset="UTF-8">  <!-- Codificación de caracteres (UTF-8 soporta acentos) -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  <!-- Para móviles -->
    <title>Título de la Página</title>  <!-- Título que aparece en la pestaña del navegador -->
</head>
<body>
    <!-- Aquí va el contenido visible: párrafos, imágenes, etc. -->
    <h1>¡Hola, Mundo!</h1>
    <p>Este es mi primer párrafo.</p>
</body>
</html>
```

- **Sintaxis clave**:
  - Etiquetas: Se abren con `<tag>` y cierran con `</tag>`. Algunas son **autocierras** como `<img />` (no necesitan cierre).
  - **DOCTYPE**: Obligatorio al inicio; le dice al navegador que use el modo HTML5.
  - `<head>`: Contiene metadatos (info invisible como título o enlaces a CSS).
  - `<body>`: El contenido visible.
  
Guarden esto como `index.html` y ábranlo en un navegador. Verán "¡Hola, Mundo!" en la página.

### 5.3. Componentes básicos

HTML5 usa **elementos** (etiquetas) para construir la página. Cada elemento tiene **atributos** para personalizarlo.

#### 5.3.1. Elementos

Los elementos son las **etiquetas** que definen el contenido. Hay dos tipos:
- **Bloque**: Ocupan todo el ancho (ej. `<div>`, `<p>` para párrafos).
- **En línea**: Solo el espacio necesario (ej. `<span>` para texto, `<a>` para enlaces).

Sintaxis: `<elemento atributo="valor">Contenido</elemento>`

Ejemplo simple:
```html
<div>Este es un bloque.</div>  <!-- Bloque genérico para secciones -->
<span>Texto en línea.</span>   <!-- En línea para partes de texto -->
```

#### 5.3.2. Atributos

Los atributos van dentro de la etiqueta de apertura, como `atributo="valor"`. Son pares clave-valor que modifican el elemento. Ejemplos comunes:
- `id="unico"`: Identificador único para un elemento (útil para CSS o JavaScript).
- `class="grupo"`: Clase para agrupar elementos (múltiples pueden compartirla).
- `src="ruta"`: Fuente para imágenes o scripts.

Sintaxis:
```html
<p id="miParrafo" class="texto-rojo">Párrafo con atributos.</p>
```

**Consejo**: Los atributos son como modificadores en un juego; cambian cómo se comporta el elemento.

#### 5.3.3. Párrafos

Los párrafos se crean con `<p>`. Agregan espacio automáticamente al final.

Sintaxis:
```html
<p>Este es un párrafo. Puede tener <strong>texto en negrita</strong> o <em>itálica</em>.</p>
<p>Segundo párrafo.</p>
```

- Elementos anidados: Como `<strong>` (negrita) o `<em>` (énfasis/itálica) para formateo básico.

#### 5.3.4. Estilos

HTML5 permite estilos inline con el atributo `style`, pero es mejor usar CSS externo (ver sección 5.4). Sintaxis inline:
```html
<p style="color: red; font-size: 18px;">Texto rojo y grande.</p>
```

- **Propiedades**: `color` (color de texto), `font-size` (tamaño de fuente), etc. Separadas por `;`.

#### 5.3.5. Tablas

Las tablas organizan datos en filas y columnas. Usan `<table>`, `<tr>` (fila), `<th>` (encabezado), `<td>` (celda).

Sintaxis básica:
```html
<table border="1">  <!-- border="1" agrega bordes (atributo obsoleto, mejor con CSS) -->
    <tr>
        <th>Nombre</th>  <!-- Encabezado -->
        <th>Edad</th>
    </tr>
    <tr>
        <td>Juan</td>    <!-- Celda de datos -->
        <td>20</td>
    </tr>
</table>
```

Esto crea una tabla simple 2x2.

#### 5.3.6. Imágenes

Las imágenes se insertan con `<img>`, que es autocierra. Atributos clave: `src` (ruta de la imagen), `alt` (texto alternativo para accesibilidad).

Sintaxis:
```html
<img src="imagen.jpg" alt="Descripción de la imagen" width="300" height="200">
```

- `width` y `height`: Tamaños en píxeles. Siempre usen `alt` para describir la imagen (importante para lectores de pantalla).

#### 5.3.7. Listas

Hay dos tipos:
- **No ordenadas** (`<ul>` para viñetas): `<ul><li>Item 1</li><li>Item 2</li></ul>`
- **Ordenadas** (`<ol>` para números): `<ol><li>Primero</li><li>Segundo</li></ol>`

Sintaxis:
```html
<ul>
    <li>Manzana</li>
    <li>Plátano</li>
</ul>
```

#### 5.3.8. Elementos de un formulario

Los formularios recolectan datos del usuario. El elemento principal es `<form>`, que envía datos a un servidor (action). Dentro: `<input>`, `<label>`, `<button>`, etc.

Sintaxis básica:
```html
<form action="/enviar" method="POST">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre">
    <button type="submit">Enviar</button>
</form>
```

- `label`: Etiqueta para el input (mejora accesibilidad).
- `for`: Vincula la label al input por su `id`.

#### 5.3.9. Tipos del elemento “input”

El `<input>` es versátil; su tipo define el comportamiento. Sintaxis: `<input type="tipo">`

Tipos comunes:
- `text`: Texto simple.
- `password`: Texto oculto (estrellitas).
- `email`: Valida email.
- `number`: Solo números.
- `radio`: Botones de opción (grupo con mismo `name`).
- `checkbox`: Casillas de verificación.
- `submit`: Botón para enviar.
- `file`: Subir archivos.

Ejemplo:
```html
<input type="email" placeholder="tu@email.com">
<input type="radio" name="opcion" value="si">
```

- `placeholder`: Texto de ejemplo que desaparece al escribir.

#### 5.3.10. Atributos del elemento “input”

Atributos clave para `<input>`:
- `name`: Nombre del campo (para enviar datos).
- `value`: Valor inicial.
- `required`: Obligatorio (valida en cliente).
- `disabled`: Deshabilita el input.
- `maxlength="10"`: Límite de caracteres.

Sintaxis:
```html
<input type="text" name="usuario" value="Invitado" required maxlength="20">
```

### 5.4. CSS

CSS separa el estilo del contenido, haciendo el HTML más limpio. Se escribe en archivos `.css` o inline.

#### 5.4.1. Módulos CSS

CSS3 se divide en módulos para funcionalidades específicas:
- **Box Model**: Define padding, border, margin (espacios alrededor de elementos).
- **Flexbox/Grid**: Para layouts responsivos (alinear elementos en filas/columnas).
- **Animations/Transitions**: Efectos suaves.
- **Media Queries**: Adaptar estilos a pantallas (ej. móviles).


#### 5.4.2. Conectar HTML y CSS

Tres formas:
1. **Inline**: `style="propiedad: valor;"` (rápido, pero no recomendado para mucho código).
2. **Interno**: En `<head>`, con `<style>contenido CSS</style>`.
3. **Externo**: Archivo `.css` enlazado con `<link rel="stylesheet" href="estilos.css">` (mejor para proyectos grandes).

Ejemplo externo (en HTML):
```html
<head>
    <link rel="stylesheet" href="estilos.css">
</head>
```

#### 5.4.3. Sintaxis de CSS

CSS usa reglas: **selector { propiedad: valor; }**

- Selector: Apunta a elementos (ver 5.4.5).
- Propiedad: Qué cambiar (ej. `color`, `background-color`).
- Valor: Cómo (ej. `red`, `#FF0000` para hex).

Ejemplo:
```css
p {
    color: blue;          /* Texto azul */
    font-size: 16px;      /* Tamaño 16 píxeles */
    text-align: center;   /* Centrado */
}
```

- Múltiples propiedades: Separadas por `;`.
- Comentarios: `/* Esto es un comentario */`.

#### 5.4.4. Variables CSS

Las variables almacenan valores reutilizables. Se declaran con `--nombre: valor;` en `:root` (global).

Sintaxis:
```css
:root {
    --color-principal: #3498db;
    --tamaño-fuente: 18px;
}

h1 {
    color: var(--color-principal);
    font-size: var(--tamaño-fuente);
}
```

Útil para temas (cambiar un valor actualiza todo).

#### 5.4.5. Selectores

Los selectores eligen qué elementos estilizar:
- **Universal**: `* { margin: 0; }` (todo).
- **Por tipo**: `p { ... }` (todos los párrafos).
- **Por clase**: `.mi-clase { ... }` (elemento con `class="mi-clase"`).
- **Por ID**: `#mi-id { ... }` (elemento con `id="mi-id"`).
- **Descendiente**: `div p { ... }` (párrafos dentro de div).
- **Pseudo-clases**: `a:hover { color: red; }` (cambio al pasar mouse).

Ejemplo:
```css
.texto-rojo {
    color: red;
}
#titulo-principal {
    font-size: 24px;
}
```

---

## Ejemplos Prácticos

### Ejemplo 1: HTML5 y CSS Completo (Sin Bootstrap)

Creemos una página simple: un currículum con tabla, lista, imagen y formulario. Guarden como `index.html` y `estilos.css`.

**index.html**:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Currículum</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1 id="titulo">Juan Pérez - Desarrollador Web</h1>
        <img src="foto.jpg" alt="Foto de perfil" width="150">
    </header>
    
    <section>
        <h2>Experiencia</h2>
        <table>
            <tr>
                <th>Año</th>
                <th>Trabajo</th>
            </tr>
            <tr>
                <td>2023</td>
                <td>Intern en Python</td>
            </tr>
            <tr>
                <td>2024</td>
                <td>Web Developer</td>
            </tr>
        </table>
    </section>
    
    <section>
        <h2>Habilidades</h2>
        <ul>
            <li>HTML5 y CSS</li>
            <li>Python básico</li>
            <li>Responsive Design</li>
        </ul>
    </section>
    
    <form action="/contacto" method="POST">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required placeholder="tu@email.com">
        <br>
        <label>Intereses:</label>
        <input type="checkbox" name="interes" value="web"> Web
        <input type="checkbox" name="interes" value="python"> Python
        <br>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

**estilos.css** (con variables):
```css
:root {
    --color-fondo: #f4f4f4;
    --color-texto: #333;
}

body {
    font-family: Arial, sans-serif;
    background-color: var(--color-fondo);
    color: var(--color-texto);
    margin: 20px;
}

#titulo {
    color: blue;
    text-align: center;
}

table {
    width: 100%;
    border-collapse: collapse;  /* Une bordes */
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #4CAF50;
    color: white;
}

ul {
    list-style-type: square;  /* Viñetas cuadradas */
}

form {
    margin-top: 20px;
}

input[type="email"] {
    width: 200px;
    padding: 5px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    border: none;
    cursor: pointer;  /* Mano al hover */
}

button:hover {
    background-color: #45a049;  /* Pseudo-clase para hover */
}
```

Abran `index.html` en el navegador. Verán una página estilizada con tabla, lista, imagen y formulario. Los estilos se aplican vía selectores (por ID, tipo, clase implícita).

### Ejemplo 2: Integrando Bootstrap

Bootstrap es un framework CSS (biblioteca de estilos prehechos) que acelera el desarrollo. **Ventajas**:
- **Responsivo por defecto**: Se adapta a cualquier dispositivo sin esfuerzo (usa media queries).
- **Componentes listos**: Botones, tablas, formularios ya estilizados; ahorra tiempo.
- **Complementa HTML**: No cambia la sintaxis de HTML; solo agrega clases (ej. `class="btn btn-primary"`) para estilos rápidos. Es ideal para principiantes porque reduce código CSS manual.
- **Grid system**: Facilita layouts en columnas (ej. 12 columnas flexibles).
- Desventaja: Archivos grandes, pero CDN (enlaces online) lo resuelven.

Para usarlo: Enlácenlo en `<head>` vía CDN (no descarguen nada).

Modifiquemos el ejemplo anterior con Bootstrap 5 (versión actual en 2025). Cambios clave:
- Agregue `<link>` a Bootstrap CSS y JS.
- Use clases como `table`, `btn`, `form-control` en lugar de CSS custom.

**bootstrap.html**:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Currículum con Bootstrap</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-4">  <!-- Clases Bootstrap: container para centrado, mt-4 para margen top -->
    <header class="text-center">
        <h1 class="display-4">Juan Pérez - Desarrollador Web</h1>  <!-- display-4 para título grande -->
        <img src="foto.jpg" alt="Foto de perfil" class="img-fluid rounded-circle" width="150">  <!-- img-fluid: responsivo, rounded-circle: circular -->
    </header>
    
    <section class="mt-3">
        <h2>Experiencia</h2>
        <table class="table table-striped table-bordered">  <!-- Clases: striped (rayas), bordered (bordes) -->
            <thead>
                <tr>
                    <th>Año</th>
                    <th>Trabajo</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>2023</td>
                    <td>Intern en Python</td>
                </tr>
                <tr>
                    <td>2024</td>
                    <td>Web Developer</td>
                </tr>
            </tbody>
        </table>
    </section>
    
    <section class="mt-3">
        <h2>Habilidades</h2>
        <ul class="list-group list-group-numbered">  <!-- list-group: lista estilizada, numbered: numerada -->
            <li class="list-group-item">HTML5 y CSS</li>
            <li class="list-group-item">Python básico</li>
            <li class="list-group-item">Responsive Design</li>
        </ul>
    </section>
    
    <form class="mt-3" action="/contacto" method="POST">
        <div class="mb-3">  <!-- mb-3: margen bottom -->
            <label for="email" class="form-label">Email:</label>
            <input type="email" class="form-control" id="email" name="email" required placeholder="tu@email.com">  <!-- form-control: estilo input -->
        </div>
        <div class="mb-3">
            <label class="form-label">Intereses:</label>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" name="interes" value="web">
                <label class="form-check-label">Web</label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" name="interes" value="python">
                <label class="form-check-label">Python</label>
            </div>
        </div>
        <button type="submit" class="btn btn-primary">Enviar</button>  <!-- btn btn-primary: botón azul -->
    </form>

    <!-- Bootstrap JS (para interacciones avanzadas, opcional aquí) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```