# Integración de Grafos - Clarividencia: Game Advisor

## 1. Contexto del Módulo
Para esta última etapa de la materia, sumamos la estructura de **Grafos** al proyecto. Aunque nuestro sistema de recomendaciones está construido principalmente sobre un Árbol Binario de Búsqueda (BST) para las consultas rápidas, sumamos este módulo para modelar las conexiones de afinidad entre juegos.

## 2. ¿Cómo se aplicaría en el Game Advisor?
Pensamos el grafo de la siguiente manera:
* **Nodos:** Cada videojuego de nuestro archivo de datos (`videojuegos.json`)
* **Aristas y Pesos:** Relaciones cruzadas (por ejemplo, juegos de la misma saga, género o desarrollador), donde el peso representa el grado de similitud.

## 3. Algoritmos implementados
* **BFS (Anchura):** Ideal para ver rutas de recomendación por saltos mínimos entre un juego y otro.
* **DFS (Profundidad):** Sirve para recorrer todas las ramificaciones posibles de una franquicia o temática de forma exhaustiva.

## 4. Conclusión
Dejamos las clases de grafos y recorridos armadas y documentadas en el repositorio para cumplir con la consigna de la materia, justificando cómo se adaptaría a nuestra red de recomendaciones de videojuegos.