# Guía de Graphviz en Python

Graphviz es un software de código abierto que usa el lenguaje DOT para describir grafos y luego generar imágenes (como PNG o PDF). En Python, podemos integrarlo para crear estas visualizaciones de forma programática.

La guía está dividida en secciones: primero, explicaremos el lenguaje DOT; luego, las formas de crear gráficos en Python; y finalmente, ejemplos prácticos con código completo.

---

## 1. El Lenguaje DOT: Grafos Dirigidos y No Dirigidos

El lenguaje DOT es un formato de texto simple para describir grafos. Un **grafo** es una estructura que consiste en **nodos** (puntos o vértices) conectados por **aristas** (líneas o edges). Hay dos tipos principales:

- **Grafo no dirigido**: Las aristas no tienen dirección (como una amistad mutua). Se declara con la palabra clave `graph`.
- **Grafo dirigido**: Las aristas tienen dirección (como un flujo de datos). Se declara con la palabra clave `digraph`.

### Sintaxis Básica de DOT

Un archivo DOT típico se ve así:

```
graph NombreDelGrafo {  // Para grafo no dirigido
    // Nodos y aristas aquí
}
```

O para dirigido:

```
digraph NombreDelGrafo {  // Para grafo dirigido
    // Nodos y aristas aquí
}
```

- **Nodos**: Se definen simplemente escribiendo su nombre. Ejemplo: `A;` (crea un nodo llamado "A").
- **Aristas**:
  - No dirigido: `A -- B;` (conecta A y B sin dirección).
  - Dirigido: `A -> B;` (conecta A hacia B).
- **Atributos**: Puedes personalizar nodos y aristas con propiedades entre corchetes `[]`.
  - Ejemplos:
    - `A [label="Nodo A", shape=box, color=red];` (cambia etiqueta, forma y color del nodo).
    - `A -> B [label="Conexión", style=dotted];` (agrega etiqueta y estilo a la arista).
- **Atributos globales**: Puedes aplicarlos a todo el grafo, nodos o aristas.
  - Ejemplo: `node [shape=circle];` (todos los nodos serán círculos).

Otros elementos comunes:
- **Subgrafos**: Para agrupar nodos, usa `subgraph { ... }`.
- **Rank**: Controla la alineación, como `rankdir=LR;` (de izquierda a derecha).
- **Etiquetas**: Puedes usar texto simple o HTML-like para etiquetas complejas.

### Sintaxis con HTML en DOT

DOT soporta etiquetas HTML-like en los atributos `label` de nodos para crear estructuras más complejas, como tablas o formatos enriquecidos. Esto no es HTML real (no usa un navegador), pero se parece.

- Usa `<` y `>` para envolver el HTML.
- Ejemplo de un nodo con tabla:

```
A [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR><TD>Encabezado</TD></TR>
    <TR><TD>Dato</TD></TR>
</TABLE>>];
```

- Atributos comunes en HTML-like:
  - `<TABLE>`: Para tablas.
  - `<TR>`: Filas.
  - `<TD>`: Celdas (puedes agregar `PORT="id"` para conectar aristas a puertos específicos).
  - `<FONT>`, `<B>`, `<I>`: Para texto en negrita, cursiva, etc.
  - `<BR/>`: Saltos de línea.

Esto permite crear "grafos" que parecen tablas, listas o estructuras visuales avanzadas.

Recuerda: DOT se guarda en un archivo con extensión `.dot`, y Graphviz lo procesa para generar imágenes.

---

## 2. Formas de Crear Gráficos en Python

En Python, puedes integrar Graphviz de dos maneras principales. Asumimos que tienes Graphviz instalado en tu sistema (descárgalo desde el sitio oficial de Graphviz) y la biblioteca `graphviz` para Python (instálala con `pip install graphviz`).

### Método 1: Crear un Archivo .dot y Renderizarlo con `os.system`

- Pasos:
  1. Genera el contenido DOT como una cadena de texto en Python.
  2. Escribe esa cadena en un archivo `.dot`.
  3. Usa `os.system` para ejecutar el comando de Graphviz y generar la imagen (ej. PNG).

- Ventajas: Simple, no requiere biblioteca extra más allá de `os`.
- Desventajas: Menos flexible para manipulación dinámica.

Ejemplo básico (código Python):

```python
import os

# Contenido DOT
dot_content = '''
digraph G {
    A -> B;
}
'''

# Escribir en archivo
with open('grafico.dot', 'w') as file:
    file.write(dot_content)

# Renderizar
os.system('dot -Tpng grafico.dot -o grafico.png')
```

Esto crea `grafico.png` desde `grafico.dot`.

### Método 2: Crear Nodos Directamente en Python con la Biblioteca `graphviz`

- Usa la biblioteca `graphviz` para crear objetos de grafo en memoria.
- Pasos:
  1. Importa `graphviz`.
  2. Crea un objeto `Graph` (no dirigido) o `Digraph` (dirigido).
  3. Agrega nodos con `node()` y aristas con `edge()`.
  4. Renderiza con `render()` o visualiza directamente.

- Ventajas: Más programático, fácil de integrar con datos dinámicos.
- Desventajas: Requiere la biblioteca instalada.

Ejemplo básico (código Python):

```python
from graphviz import Digraph

# Crear grafo dirigido
g = Digraph('G')

# Agregar nodos y arista
g.node('A')
g.node('B')
g.edge('A', 'B')

# Renderizar a PNG
g.render('grafico', format='png', view=True)  # view=True abre la imagen
```

Esto genera `grafico.png` directamente.

En ambos métodos, puedes personalizar atributos pasando diccionarios o cadenas.

---

## 3. Ejemplos Prácticos


Graficar la lista enlazada doble con ambos metodos. 

- **Grafica esperada**
```
digraph G{

  rankdir=LR; 
  node[shape=egg, style=filled, color=khaki, fontname="Century Gothic"]; graph [fontname = "Century Gothic"];
  labelloc="t"; label = "Lista Doble Enlazada - Cursos";
  x1[dir=both label="Codigo =1\nNombre = Matemáticas \nCreditos = 4"]
  x2[dir=both label="Codigo =2\nNombre = Física \nCreditos = 5"]
  x3[dir=both label="Codigo =3\nNombre = Programación \nCreditos = 3"]
  x1 -> x2
  x1 -> x3
  x2 -> x3
  x2 -> x1
  x3 -> x1
  x3 -> x2

}

```
