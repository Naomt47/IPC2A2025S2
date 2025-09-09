# Guía de Expresiones Regulares (Regex) en Python

 

Esta semana nos enfocamos en **expresiones regulares** (regex), una herramienta utilizada para buscar, validar y manipular texto en Python. Regex puede parecer complicada al principio, pero piensen en ella como un "filtro inteligente" para cadenas de texto: permite encontrar patrones específicos, como emails o números de teléfono, de forma eficiente.



**Importante**: Para usar regex en Python, importamos el módulo `re` (como en el script: `import re`). Este módulo proporciona funciones como `search`, `findall`, `sub`, etc. Siempre definimos un **patrón** (una cadena con sintaxis especial de regex, marcada con `r""` para "raw string", que evita que Python interprete las barras invertidas `\` de forma especial).

---

## 1. Introducción a Expresiones Regulares y el Módulo `re`

Las expresiones regulares son un lenguaje para definir **patrones** que coinciden con partes de una cadena de texto. En Python, usamos el módulo `re` para aplicarlas. Un patrón es como una plantilla (ej. "busca una palabra de 3 letras") que Python compara contra un texto.

**Uso del módulo `re`**:
- Importar: `import re`
- Funciones principales:
  - **`re.search(patron, cadena)`**: Busca la primera coincidencia del patrón en la cadena. Devuelve un objeto `Match` o `None`.
  - **`re.findall(patron, cadena)`**: Encuentra todas las coincidencias y devuelve una lista.
  - **`re.split(patron, cadena)`**: Divide la cadena usando el patrón como separador.
  - **`re.sub(patron, reemplazo, cadena)`**: Reemplaza coincidencias por otro texto.
  - **`re.match(patron, cadena)`**: Verifica si el patrón coincide desde el inicio de la cadena.
  - **`re.compile(patron)`**: Compila un patrón para reutilizarlo, mejorando eficiencia.

**Sintaxis básica**:
- Los patrones se escriben como cadenas con prefijo `r` (raw string): `r"patrón"`. Esto evita que Python interprete las barras invertidas (`\`) como escapes.
- Ejemplo: `r"hola"` busca la palabra literal "hola".


---

## 2. Sintaxis de Expresiones Regulares

El script `regex.py` cubre varias construcciones de regex. A continuación, los temas principales y su sintaxis:

### 2.1. Búsqueda Literal de Palabras

**Concepto**: Buscar una palabra exacta en una cadena. Es el caso más simple, donde el patrón es el texto literal.

**Sintaxis**:
- Patrón: `r"texto"`. Coincide exactamente con "texto".
- Ejemplo: `r"hola"` coincide con "hola" en cualquier parte de la cadena.

**Uso en el script**:
- Busca "hola" en "hola mundo" con `re.search`. Útil para verificar si una palabra existe.



### 2.2. Anclas (^ y $)

**Concepto**: Las anclas fijan el patrón a una posición específica en la cadena.
- `^`: Coincide al **inicio** de la cadena.
- `$`: Coincide al **fin** de la cadena.

**Sintaxis**:
- `^texto`: Coincide si la cadena empieza con "texto".
- `texto$`: Coincide si termina con "texto".
- `^texto$`: Coincide si la cadena es exactamente "texto".

**Uso en el script**:
- `r"^hola"`: Verifica si la cadena empieza con "hola".
- `r"mundo$"`: Verifica si termina con "mundo".
- Usados con `re.search` para validar posiciones específicas.

**Consejo**: Úsenlos para validaciones estrictas, como un formato exacto (ej. un código que siempre empieza con "ABC").

### 2.3. Metacaracteres y Secuencias Especiales (\b, \w, \s, \d)

**Concepto**: Los metacaracteres son símbolos con significado especial. La barra invertida (`\`) define secuencias especiales o escapa metacaracteres.

**Sintaxis**:
- **`\b`**: Límite de palabra. Marca el inicio o fin de una palabra (entre caracteres alfanuméricos y no alfanuméricos, como espacios o puntuación).
  - Ejemplo: `r"\bhola\b"` coincide con "hola" como palabra completa, no con "holanda".
- **`\w`**: Carácter alfanumérico (letras a-z, A-Z, números 0-9, guion bajo `_`).
  - Ejemplo: `r"\w+"` coincide con una palabra (una o más letras/números).
- **`\s`**: Espacio en blanco (espacios, tabuladores, saltos de línea).
  - Ejemplo: `r"\s+"` coincide con uno o más espacios.
- **`\d`**: Dígito (0-9).
  - Ejemplo: `r"\d+"` coincide con números como "123".
- **Escapar metacaracteres**: `\` antes de un metacaractér (ej. `\.` para un punto literal, ya que `.` solo significa "cualquier carácter").

**Uso en el script**:
- `r"\b\w+\b"`: Encuentra todas las palabras completas (letras/números) con `re.findall`.
- `r"\s+"`: Divide la cadena en palabras usando espacios con `re.split`.
- `r"\w+@\w+\.\w+"`: Usa `\w` y `\.` para capturar emails (nombre@dominio.com).
- `r"\d{3}-\d{3}-\d{4}"`: Valida números de teléfono con `\d`.



### 2.4. Cuantificadores (+, *, ?, {n})

**Concepto**: Los cuantificadores indican cuántas veces se repite un carácter o grupo.

**Sintaxis**:
- `+`: Uno o más. Ej: `r"a+"` coincide con "a", "aa", "aaa".
- `*`: Cero o más. Ej: `r"a*"` coincide con "", "a", "aa".
- `?`: Cero o una vez. Ej: `r"a?"` coincide con "" o "a".
- `{n}`: Exactamente n veces. Ej: `r"\d{3}"` coincide con "123".
- `{n,m}`: Entre n y m veces. Ej: `r"\d{2,4}"` coincide con "12", "123", "1234".

**Uso en el script**:
- `r"\w+"`: Una o más letras/números (palabras).
- `r"\s+"`: Uno o más espacios.
- `r"\d{3}-\d{3}-\d{4}"`: Tres dígitos, guion, tres dígitos, guion, cuatro dígitos (teléfono).


### 2.5. Grupos de Captura

**Concepto**: Los paréntesis `()` agrupan partes del patrón para extraerlas o estructurar el regex. Cada grupo se numera (1, 2, ...).

**Sintaxis**:
- `(patrón)`: Captura lo que coincide con el patrón.
- Acceso: Con `resultado.group(n)` (`n` es el número del grupo; `group(0)` es la coincidencia completa).
- Ejemplo: `r"(\w+)@(\w+\.\w+)"` captura el nombre y dominio de un email.

**Uso en el script**:
- `r"(\w+)@(\w+\.\w+)"`: Captura el nombre (antes de `@`) y dominio (después de `@`, incluyendo el punto literal). Usado con `re.search` y `group(1)`, `group(2)`.

**Consejo**: Piensen en grupos como "guardar partes" para usarlas después. Útil para extraer datos estructurados (ej. fechas, nombres).

### 2.6. Escapar Metacaracteres (\)

**Concepto**: La barra invertida `\` quita el significado especial de metacaracteres como `.`, `*`, `+`.

**Sintaxis**:
- `\.`: Coincide con un punto literal (en lugar de "cualquier carácter").
- Ejemplo: `r"\w+\.\w+"` coincide con "example.com" (punto literal).

**Uso en el script**:
- En el patrón de email, `\.` asegura que el punto sea literal (`example.com`, no `exampleXcom`).

**Consejo**: Siempre escapen metacaracteres cuando quieran su valor literal. Lista común: `. * + ? | () [] {} ^ $`.

### 2.7. Búsqueda Insensible a Mayúsculas/Minúsculas (re.IGNORECASE)

**Concepto**: Permite que el patrón coincida sin distinguir entre mayúsculas y minúsculas.

**Sintaxis**:
- Usar el flag `re.IGNORECASE` (o `re.I`) en funciones como `re.findall(patron, cadena, re.IGNORECASE)`.
- Ejemplo: `r"python"` con `re.IGNORECASE` coincide con "Python", "PYTHON", "pYtHoN".

**Uso en el script**:
- Busca "python" en "Me encanta Python y python" con `re.findall` y `re.IGNORECASE`, capturando ambas formas.

**Consejo**: Ideal para búsqueda de texto en datos reales (ej. formularios donde usuarios escriben variado).

### 2.8. Validación con Patrones Exactos

**Concepto**: Combinar anclas (`^`, `$`) y patrones específicos para validar formatos exactos (ej. número de teléfono).

**Sintaxis**:
- Ejemplo: `r"^\d{3}-\d{3}-\d{4}$"` valida "123-456-7890" (tres dígitos, guion, tres dígitos, guion, cuatro dígitos, nada más).
- Usar con `re.match` (coincide desde el inicio) o `re.search` con `^` y `$`.

**Uso en el script**:
- Valida teléfonos con `r"^\d{3}-\d{3}-\d{4}"` usando `re.match`.

**Consejo**: Para validaciones, siempre usen `^` y `$` para evitar coincidencias parciales. Prueben con "123-456-7890abc" (debería fallar).

### 2.9. Compilación de Patrones (re.compile)

**Concepto**: Compilar un patrón en un objeto reusable mejora eficiencia cuando se usa repetidamente.

**Sintaxis**:
- `patron_compilado = re.compile(r"patrón")`
- Usar: `patron_compilado.match(cadena)` o `patron_compilado.search(cadena)`.

**Uso en el script**:
- Compila `r"^\d{3}-\d{3}-\d{4}"` y lo usa en un bucle para validar múltiples teléfonos, evitando recompilar el patrón.

**Consejo**: Úsenlo en bucles o funciones que repiten el mismo patrón. No es necesario para una sola búsqueda.

---

## 3. Uso del Módulo `re` en el Script

El script muestra cómo aplicar regex en tareas comunes. Aquí, el uso general de las funciones:

- **`re.search`**: Busca la primera coincidencia en cualquier parte. Usada para verificar palabras, inicios/fines y emails. Devuelve un objeto `Match` con métodos como `group()` para extraer partes.
- **`re.findall`**: Encuentra todas las coincidencias no solapadas. Usada para listas de palabras o coincidencias insensibles a mayúsculas.
- **`re.split`**: Divide la cadena en una lista usando el patrón como separador. Ideal para tokenizar (ej. palabras separadas por espacios).
- **`re.sub`**: Reemplaza coincidencias por nuevo texto. Útil para limpieza o transformación de texto.
- **`re.match`**: Verifica desde el inicio. Perfecto para validaciones estrictas (ej. formato de teléfono).
- **`re.compile`**: Optimiza patrones repetidos, usado en un bucle para validar múltiples entradas.



---

## 4. Ejemplo Práctico Integrado

Aquí va un ejemplo que combina los conceptos del script, para que lo prueben. Crea un archivo `ejemplo_regex.py`:

```python
import re

# Datos de ejemplo
texto = "Contactos: juan@example.com, 123-456-7890, Hola Python, maria@web.co.uk"

# 1. Encontrar emails (grupos de captura, \w, \.)
patron_email = r"(\w+)@(\w+\.\w+\.?\w*)"
emails = re.findall(patron_email, texto)
print("Emails:", [(nombre, dominio) for nombre, dominio in emails])

# 2. Validar teléfono (anclas, \d, {n})
patron_telefono = r"^\d{3}-\d{3}-\d{4}$"
telefono = "123-456-7890"
print("Teléfono válido" if re.match(patron_telefono, telefono) else "Teléfono inválido")

# 3. Dividir palabras (\s, \b)
patron_palabras = r"\b\w+\b"
palabras = re.findall(patron_palabras, texto, re.IGNORECASE)
print("Palabras:", palabras)

# 4. Reemplazar "Python" por "Java" (\b, re.IGNORECASE)
nuevo_texto = re.sub(r"\bPython\b", "Java", texto, flags=re.IGNORECASE)
print("Texto modificado:", nuevo_texto)
```

**Salida**:
```
Emails: [('juan', 'example.com'), ('maria', 'web.co.uk')]
Teléfono válido
Palabras: ['Contactos', 'juan', 'example', 'com', '123', '456', '7890', 'Hola', 'Python', 'maria', 'web', 'co', 'uk']
Texto modificado: Contactos: juan@example.com, 123-456-7890, Hola Java, maria@web.co.uk
```

**Explicación**:
- Combina grupos de captura (emails), anclas (teléfono), límites de palabra, e insensibilidad a mayúsculas.
- Usa `findall`, `match`, y `sub`, mostrando versatilidad.

---

## 5. Consejos y Buenas Prácticas para Principiantes

- **Usen `r""`**: Siempre definan patrones con cadenas crudas (`r"patrón"`) para evitar problemas con `\`.
- **Prueben en sitios**: Usen regex101.com para visualizar patrones.
- **Empiecen simple**: Comiencen con literales (`r"hola"`) antes de metacaracteres complejos.
- **Validen con `^` y `$`**: Para formatos exactos, siempre usen anclas.
- **Eviten exceso**: Regex es potente pero lento para cosas simples (ej. usar `str.find()` para literales).

---

## 6. Ejercicios para Practicar

1. **Básico**: Escriban un patrón para encontrar fechas en formato "DD-MM-YYYY" (ej. "01-12-2023"). Usen `\d` y `{n}`.
2. **Intermedio**: Usen `re.sub` para reemplazar espacios múltiples por uno solo en una cadena.
3. **Avanzado**: Validen una contraseña que tenga al menos 8 caracteres, una letra mayúscula, una minúscula, y un número. Usen grupos y cuantificadores.



