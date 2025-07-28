# Variables

## Nombres de Variables

El identificador debe comenzar por una letra o _. El resto puede ser alfanumérico y también puede contener _. 
    
- identificadores bien construidos:
```python
numero
_numero
numero3
numero_3
primer_apellido
primerApellido
```

- identificadores mal construidos:
```python
3numero
primer apellido
&numero
primer%apellido
```

### Casesensitive
Python distingue entre mayusculas y minúsculas

```py
numero = 5
Numero = 9
nuMero = 0
 
print(Numero)
```

### Convención de Nomenclatura

- **camelCase:**
    - El principio de cada nueva palabra va con mayuscula
    ```python
    #Definiendo una variable con formato camelCase:
    nombreDeTuVariable = "Holis"
    ```

- **snake_case:**
    - se utiliza guión bajo en lugar de espacio para separar las palabras
    ```python
    #Definiendo una variable con formato camelCase:
    nombre_de_tu_variable = "Holis"
    ```
