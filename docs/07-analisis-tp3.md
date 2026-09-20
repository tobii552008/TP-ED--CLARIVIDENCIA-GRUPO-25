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

## 2.B)  Conclusión

El BST optimiza las búsquedas recurrentes en *Clarividencia*. A diferencia de la búsqueda binaria en listas, permite insertar nuevos juegos manteniendo la estructura ordenada sin tener que reordenar toda la lista.

## 3. PRUEBA DEL ARBOL  

Salida de `python algoritmos/probar_bst.py`: 

--- Probando Búsqueda ---
Encontrado: God of War

--- Altura del árbol ---
Altura: 5

--- inorder (ordenado alfabéticamente) ---
  Celeste
  Cyberpunk 2077
  Elden Ring
  God of War
  Hadès
  Hollow Knight
  Minecraft
  Portal 2
  Red Dead Redemption 2
  The Witcher 3: Wild Hunt

--- preorder ---
  The Witcher 3: Wild Hunt
  Hollow Knight
  Elden Ring
  Celeste
  Cyberpunk 2077
  God of War
  Hadès
  Red Dead Redemption 2
  Minecraft
  Portal 2

--- postorder ---
  Cyberpunk 2077
  Celeste
  Hadès
  God of War
  Elden Ring
  Portal 2
  Minecraft
  Red Dead Redemption 2
  Hollow Knight
  The Witcher 3: Wild Hunt

## 4. Comparacion de tiempos 

Los tiempos son reales, sacados con `algoritmos/medir_tiempos.py´. cada valor es el promedio de 2000 busquedas, en milisegundos. Se busca el ultimo juego de la lista (mezclada con semilla 42), que es el peor caso de la busqueda secuencial. El ordenamiento de la lista para la binaria y la construccion del arbol no se miden. Los valores varian un poco entre corridas. 

  N |  secuencial_ms |  binaria_ms |  arbol_ms
     100 |        0.00711 |     0.00098 |   0.00168
    1000 |        0.07937 |     0.00158 |   0.00752
   10000 |        1.07821 |     0.00219 |   0.00174
  100000 |       23.34469 |     0.00267 |   0.00233 
    
## 5. Análisis de complejidad

- **Búsqueda secuencial:** O(n). Recorre toda la lista en el peor caso.
- **Búsqueda binaria:** O(log n), pero exige la lista ordenada. Ordenar cuesta O(n log n) una sola vez.
- **Búsqueda en árbol:** O(log n) en promedio si el árbol está balanceado, y O(n) en el peor caso si está degenerado (queda como una lista).
- **Inserción en árbol:** O(log n) en promedio, y O(n) en el peor caso.
- **Inserción en lista ordenada:** O(n), porque hay que correr los elementos que vienen después.
- **Recorridos (inorder, preorder, postorder):** O(n), porque visitan cada nodo una sola vez.

## 6. conclucion 
Con muchos juegos, la búsqueda secuencial es la más lenta: con 100.000 juegos tardó 23,3 ms. La binaria y el árbol dieron tiempos parecidos: 0,00267 ms y 0,00233 ms. Por lo tanto, la velocidad de búsqueda no es lo que decide, sino el costo de agregar juegos. Nos quedamos con BST porque en el caso hipotético de que un usuario agregue un juego nuevo, por ejemplo: For Honor, en la lista ordenada hay que correr los demás elementos o volver a ordenar, y en el árbol solo se baja comparando y colgándose en el nodo correspondiente. En la lista ordenada agregar cuesta O(n), y en el árbol O(log n) en promedio, pero si los juegos ya se insertan ordenados, el árbol queda en fila como una lista y buscar pasa a ser O(n). De igual manera los árboles AVL pueden solucionar ese problema.  

## 7. Errores o dudas que tuvimos

1. **Búsqueda con `in` en el árbol.** La búsqueda usaba `if titulo in titulo_actual`, que acepta texto parcial, pero el árbol ordena por el título completo. Al buscar "war", la comparación lo mandaba por el lado derecho (la "w" viene después de la "t" de "The Witcher") y no encontraba "God of War", aunque estaba en el árbol. Lo cambiamos a `if titulo == titulo_actual`, que exige el título exacto.
2. **`return None` dentro del `while`.** En la búsqueda binaria, el `return None` quedó adentro del `while` por un error de indentación, y no encontraba juegos que existían. Lo movimos un tab a la izquierda, afuera del bucle.
3. **Código fuera del `for`.** En `medir_tiempos.py`, parte del código quedó fuera del `for` y salía una sola fila de la tabla. Lo arreglamos agregando el tab que faltaba. 
