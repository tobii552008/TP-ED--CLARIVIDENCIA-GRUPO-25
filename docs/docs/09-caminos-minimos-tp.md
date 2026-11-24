# Caminos Mínimos - Clarividencia: Game Advisor

## 1. Contexto del Módulo
Sobre el grafo de afinidad entre videojuegos (ver `08-grafos-tp.md`) sumamos un algoritmo de **camino mínimo**. Igual que con el grafo, queda implementado y documentado en el repositorio, pero no está integrado al menú de la terminal.

## 2. ¿Qué significa "costo" en nuestro dominio?
En el grafo, el peso de una arista representa el **grado de similitud** entre dos juegos (más peso = más parecidos). Como Dijkstra busca la suma **mínima**, usamos el inverso:

`costo = 1 / similitud`

Así, dos juegos muy parecidos están "cerca" (costo bajo) y un camino mínimo es la cadena de recomendaciones más afín entre un juego de origen y uno de destino. La similitud debe ser mayor que cero, porque en la matriz de adyacencia el valor 0 significa "sin arista".

## 3. Algoritmo elegido: Dijkstra
Elegimos Dijkstra por las propiedades de nuestro grafo:
* **Pesos no negativos:** el costo `1 / similitud` siempre es positivo, que es la condición que exige Dijkstra. Por eso no hace falta Bellman-Ford.
* **No dirigido y ponderado:** BFS no sirve, porque solo minimiza la cantidad de aristas y las nuestras tienen costos distintos.
* **Representación:** usamos la versión simple sobre `GrafoMatriz`, que no necesita una cola de prioridad.

## 4. Complejidad
* **Nuestra implementación (matriz, sin heap):** O(V²). Se recorre toda la lista de nodos para elegir el de menor distancia, V veces.
* **Con lista de adyacencia y heap:** O((V + E) log V). Convendría si el catálogo creciera a miles de juegos con un grafo ralo.
* Con 24 juegos en el catálogo, V² = 576 operaciones, por lo que la diferencia es irrelevante.
* **Espacio:** O(V) adicional para distancias, padres y nodos procesados.

## 5. Implementación
* Archivo: `algoritmos/caminos.py`
* `CaminosMinimos.dijkstra(grafo, origen)`: devuelve las distancias mínimas y los padres.
* `CaminosMinimos.camino_minimo(grafo, origen, destino)`: reconstruye el camino y su costo total.
* `similitud_a_costo(similitud)`: convierte similitud en costo.
* Caso de prueba: ejecutar `python algoritmos/caminos.py`.

## 6. Conclusión
Dejamos Dijkstra implementado y probado sobre `GrafoMatriz`, con el costo del dominio definido y la elección justificada, para cumplir con la consigna. Su integración a la terminal quedaría como extensión futura.