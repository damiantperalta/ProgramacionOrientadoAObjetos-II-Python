# Trabajo Práctico 2 – Interfaz Gráfica con Python

## Integrantes del grupo
- **Damián Peralta**  
- **Lucas Morilla**  
- **Luis Calegari**  

## Carrera
Licenciatura en Informática

## Materia
Programación con Objetos 2

## Profesores
- Marcela Toba  
- José Luis Cabrera  

---

## Casos de Prueba

### 1. Ingresar relaciones válidas
**Descripción:** Ingresar relaciones entre diferentes personas utilizando los tipos de relación válidos (`amigo personal`, `conocido`, `compañero`).  
**Pasos:**
1. Elegir la opción “Ingresar relaciones de amistad” del menú.  
2. Ingresar un **1** para Grafo 1 o un **2** para Grafo 2.  
3. Ingresar nombre de la primera persona y luego el de la segunda.  
4. Ingresar un tipo de relación válido.  

**Expectativa:**  
Se agrega la relación correctamente al grafo seleccionado y aparece el mensaje:  
> “Se agregó la relación (tipo) entre (persona1) y (persona2) en el grafo n”.

---

### 2. Intento de ingresar relaciones con nombres repetidos
**Descripción:** No permitir relaciones donde los nombres de las dos personas son idénticos.  
**Pasos:**
1. Elegir la opción “Ingresar relaciones de amistad”.  
2. Seleccionar Grafo 1 o 2.  
3. Ingresar el mismo nombre para ambas personas.  

**Expectativa:**  
El programa no lo permite y aparece el mensaje:  
> “No puedes ingresar dos personas con el mismo nombre”.

---

### 3. Calcular la distancia de amistad inexistente
**Descripción:** Intentar calcular la distancia entre dos personas que no están conectadas.  
**Pasos:**
1. Elegir “Calcular la distancia de amistad”.  
2. Seleccionar Grafo 1 o 2.  
3. Ingresar los nombres de dos personas no conectadas.  

**Expectativa:**  
El programa muestra:  
> “No existe un camino entre estas dos personas.”

---

### 4. Ingresar un tipo de relación no válido
**Descripción:** Intentar ingresar un tipo de relación distinto a los aceptados.  
**Pasos:**
1. Elegir “Ingresar relaciones de amistad”.  
2. Seleccionar Grafo 1 o 2.  
3. Ingresar los nombres de dos personas.  
4. Ingresar un tipo de relación inválido.  

**Expectativa:**  
El programa muestra:  
> “Tipo de relación no válido. Por favor, ingresa 'amigo personal', 'conocido' o 'compañero'.”

---

### 5. Visualizar grafo con relaciones ingresadas
**Descripción:** Visualizar el grafo después de ingresar varias relaciones.  
**Pasos:**
1. Ingresar varias relaciones válidas.  
2. Elegir “Mostrar el grafo”.  
3. Seleccionar el grafo 1 o 2.  

**Expectativa:**  
Se muestra correctamente el grafo con todas las relaciones, nodos (personas) y aristas (relaciones con peso).

---

### 6. Calcular distancia con una sola persona
**Descripción:** Intentar calcular la distancia de amistad con solo una persona existente.  
**Pasos:**
1. Elegir “Calcular la distancia de amistad”.  
2. Seleccionar Grafo 1 o 2.  
3. Ingresar el nombre de una persona existente.  
4. Ingresar un nombre inexistente o vacío.  

**Expectativa:**  
El programa muestra un mensaje de error indicando que la segunda persona no existe en el grafo.

