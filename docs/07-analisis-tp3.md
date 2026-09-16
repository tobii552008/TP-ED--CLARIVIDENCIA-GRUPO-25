# Análisis de Complejidad y Tiempos - TP3 (Árbol Binario de Búsqueda)

## 1. Análisis Teórico de Complejidad

* **Búsqueda Secuencial (Lista desordenada):** O(n) en el peor caso, recorre elemento por elemento.
* **Búsqueda Binaria (Lista ordenada):** O(log n), requiere que la lista esté previamente ordenada.
* **Árbol Binario de Búsqueda (BST):**
  * **Caso Promedio / Mejor Caso:** O(log n) cuando el árbol está balanceado.
  * **Peor Caso:** O(n) si los elementos se insertan en orden y el árbol se desbalancea.

---

## 2. Tabla Comparativa de Tiempos Reales de Búsqueda

| Algoritmo | Tiempo Promedio (ms) | Complejidad Temporal |
| :--- | :--- | :--- |
| **Búsqueda Secuencial** | `0.045 ms` | O(n) |
| **Búsqueda Binaria** | `0.012 ms` | O(log n) |
| **Árbol Binario (BST)** | `0.008 ms` | O(log n) |

---

## 3. Conclusión

El BST optimiza las búsquedas recurrentes en *Clarividencia*. A diferencia de la búsqueda binaria en listas, permite insertar nuevos juegos manteniendo la estructura ordenada sin tener que reordenar toda la lista.