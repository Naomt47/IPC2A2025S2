# Guía de Comandos de Git

## Inicialización y Configuración de un Repositorio

### Crear un nuevo repositorio local
#### `git init`
- Inicializa un nuevo repositorio de Git en el directorio actual. Crea una carpeta oculta `.git` que contiene toda la estructura necesaria para el control de versiones.
- **Ejemplo**:
  ```bash
  git init
  ```

### Enlazar un repositorio local con uno remoto
#### `git remote add origin <urlRepositorio>`
- Conecta el repositorio local con un repositorio remoto (por ejemplo, en GitHub, GitLab o Bitbucket). La URL debe ser la dirección del repositorio remoto.
- **Ejemplo**:
  ```bash
  git remote add origin https://github.com/usuario/repositorio.git
  ```

---

## Gestión de Archivos y Cambios

### Agregar archivos al área de preparación
#### `git add <archivo>`
- Añade un archivo específico.
- **Ejemplo**:
  ```bash
  git add index.html
  ```

#### `git add -A`
- Añade todos los archivos modificados, nuevos o eliminados.
- **Ejemplo**:
  ```bash
  git add -A
  ```

### Confirmar cambios
#### `git commit -m "<mensaje>"`
- Guarda los cambios en el historial del repositorio con un mensaje descriptivo que explica los cambios realizados.
- **Ejemplo**:
  ```bash
  git commit -m "mi cambio"
  ```

#### `git commit -am "<mensaje>"`
- Combina `git add -A` y `git commit` en un solo paso. Añade todos los archivos modificados (no nuevos) y realiza el commit con el mensaje proporcionado. Útil para cambios rápidos.
- **Ejemplo**:
  ```bash
  git commit -am "Se resolvió el conflicto de los colores"
  ```

### Ver el estado del repositorio
#### `git status`
- Muestra el estado actual del repositorio, incluyendo los archivos modificados, los que están en el área de preparación y los que no están siendo rastreados.
- **Ejemplo**:
  ```bash
  git status
  ```

### Comparar cambios
#### `git diff`
- Muestra las diferencias entre los cambios realizados en los archivos y el estado anterior en el repositorio. Ideal para revisar modificaciones antes de añadirlas al área de preparación.
- **Ejemplo**:
  ```bash
  git diff
  ```

---

## Trabajo con Repositorios Remotos

### Clonar un repositorio remoto
#### `git clone <urlRepositorio>`
- Crea una copia local de un repositorio remoto, incluyendo todo su historial y ramas.
- **Ejemplo**:
  ```bash
  git clone https://github.com/usuario/repositorio.git
  ```

### Enviar cambios al repositorio remoto
#### `git push origin <rama>`
- Envía los commits locales de la rama especificada al repositorio remoto. En este caso, `origin` es el nombre del repositorio remoto y `master` (o `main`) es la rama.
- **Ejemplo**:
  ```bash
  git push origin master
  ```

---

## Gestión de Ramas

### Listar ramas
#### `git branch`
- Muestra una lista de todas las ramas locales en el repositorio. La rama actual está marcada con un asterisco (*).
- **Ejemplo**:
  ```bash
  git branch
  ```

### Crear una nueva rama
#### `git branch <nombre_rama>`
- Crea una nueva rama con el nombre especificado, pero no cambia a ella automáticamente.
- **Ejemplo**:
  ```bash
  git branch Pruebas
  ```

### Cambiar de rama
#### `git checkout <nombre_rama>`
- Cambia a la rama especificada, actualizando el directorio de trabajo con el contenido de esa rama.
- **Ejemplo**:
  ```bash
  git checkout Pruebas
  ```

#### `git switch <nombre_rama>`
- Similar a `git checkout`, pero más específico para cambiar de rama. Es una alternativa moderna introducida en versiones recientes de Git.
- **Ejemplo**:
  ```bash
  git switch Pruebas
  ```

### Fusionar ramas
#### `git checkout main` seguido de `git merge <nombre_rama>`
- Cambia a la rama principal (`main`) y fusiona los cambios de la rama especificada en ella. Esto combina el historial de ambas ramas.
- **Ejemplo**:
  ```bash
  git checkout main
  git merge Pruebas
  ```

---

## Resolución de Conflictos

### Manejo de conflictos
- Si al fusionar ramas (`git merge`) hay conflictos (por ejemplo, cambios en las mismas líneas de un archivo), Git pausará la fusión y marcará los archivos conflictivos. Debes:
  1. Abrir los archivos conflictivos en un editor (como Visual Studio Code).
  2. Resolver manualmente los conflictos, eligiendo qué cambios conservar.
  3. Marcar los archivos como resueltos usando `git add <archivo>`.
  4. Finalizar la fusión con un commit.
- **Ejemplo**:
  ```bash
  git add archivo_conflictivo.txt
  git commit -am "Se resolvió el conflicto de los colores"
  ```

---

## Inspección del Historial

### Ver el historial de commits
#### `git log`
- Muestra el historial de commits en la rama actual, incluyendo el autor, la fecha y el mensaje de cada commit. Usa la tecla `Espacio` para desplazarte y `q` para salir.
- **Ejemplo**:
  ```bash
  git log
  ```

### Obtener ayuda sobre comandos
#### `git help <comando>`
- Muestra la documentación oficial de Git para el comando especificado. Útil para explorar opciones adicionales.
- **Ejemplo**:
  ```bash
  git help log
  ```

---

## Flujo Básico para Crear y Enlazar un Repositorio

1. **Crear un repositorio local**:
   ```bash
   git init
   ```

2. **Añadir archivos iniciales**:
   ```bash
   git add -A
   ```

3. **Hacer el primer commit**:
   ```bash
   git commit -m "Inicialización del repositorio"
   ```

4. **Enlazar con un repositorio remoto**:
   ```bash
   git remote add origin https://github.com/usuario/repositorio.git
   ```

5. **Enviar los cambios al repositorio remoto**:
   ```bash
   git push origin main
   ```

---
