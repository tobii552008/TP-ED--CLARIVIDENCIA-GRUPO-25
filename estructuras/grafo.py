from collections import deque

class GrafoMatriz:
    """
    Representación clásica de un grafo utilizando una matriz de adyacencia (lista de listas).
    Ideal para grafos densos o consultas rápidas de aristas.
    """
    def __init__(self, cantidad_nodos, dirigido=False):
        self.n = cantidad_nodos
        self.dirigido = dirigido
        # Inicializamos la matriz con ceros (sin conexiones al principio)
        self.matriz = [[0] * self.n for _ in range(self.n)]

    def agregar_arista(self, nodo_u, nodo_v, peso=1):
        # Conectamos el nodo U con el V
        self.matriz[nodo_u][nodo_v] = peso
        # Si el grafo no es dirigido, hacemos el camino de vuelta también
        if not self.dirigido:
            self.matriz[nodo_v][nodo_u] = peso

    def eliminar_arista(self, nodo_u, nodo_v):
        # Ponemos en cero para borrar la conexión
        self.matriz[nodo_u][nodo_v] = 0
        if not self.dirigido:
            self.matriz[nodo_v][nodo_u] = 0

    def hay_arista(self, nodo_u, nodo_v):
        # Devuelve True si hay peso distinto de cero (están conectados)
        return self.matriz[nodo_u][nodo_v] != 0

    def obtener_vecinos(self, nodo_u):
        # Recorre la fila buscando columnas con peso (vecinos efectivos)
        return [columna for columna in range(self.n) if self.matriz[nodo_u][columna] != 0]


class RecorridosGrafos:
    """
    Clase contenedora para los algoritmos de recorrido en grafos (BFS y DFS).
    """

    @staticmethod
    def recorrido_anchura_bfs(grafo, nodo_inicio):
        """
        Recorrido BFS (en anchura / por niveles tipo onda expansiva).
        Usa una cola para ir visitando los vecinos de forma ordenada.
        """
        visitados = {nodo_inicio}
        cola = deque([nodo_inicio])
        orden_recorrido = []
        
        while cola:
            nodo_actual = cola.popleft()
            orden_recorrido.append(nodo_actual)
            
            # Revisamos los vecinos de este nodo
            for vecino in grafo.obtener_vecinos(nodo_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
                    
        return orden_recorrido

    @staticmethod
    def recorrido_profundidad_dfs_iterativo(grafo, nodo_inicio):
        """
        Recorrido DFS (en profundidad) de forma iterativa utilizando una pila.
        """
        visitados = set()
        pila = [nodo_inicio]
        orden_recorrido = []
        
        while pila:
            nodo_actual = pila.pop()
            
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                orden_recorrido.append(nodo_actual)
                
                # Apilamos los vecinos en orden inverso para mantener la coherencia de la pila
                vecinos = grafo.obtener_vecinos(nodo_actual)
                for vecino in reversed(vecinos):
                    if vecino not in visitados:
                        pila.append(vecino)
                        
        return orden_recorrido