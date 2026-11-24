import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

INFINITO = float('inf')


def similitud_a_costo(similitud):
   
    if similitud <= 0:
        raise ValueError
    return 1 / similitud


class CaminosMinimos:
   

    @staticmethod
    def dijkstra(grafo, origen):
       
        n = grafo.n
        distancias = [INFINITO] * n
        padres = [None] * n
        procesados = [False] * n
        distancias[origen] = 0

        for _ in range(n):
            # Nodo no procesado con menor distancia conocida
            actual = None
            for nodo in range(n):
                if not procesados[nodo] and (actual is None or distancias[nodo] < distancias[actual]):
                    actual = nodo

            # Si lo mejor que queda es infinito, el resto es inalcanzable
            if actual is None or distancias[actual] == INFINITO:
                break

            procesados[actual] = True

            # Relajacion de los vecinos
            for vecino in grafo.obtener_vecinos(actual):
                costo = grafo.matriz[actual][vecino]
                if costo < 0:
                    raise ValueError
                nueva_distancia = distancias[actual] + costo
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    padres[vecino] = actual

        return distancias, padres

    @staticmethod
    def camino_minimo(grafo, origen, destino):
       
        distancias, padres = CaminosMinimos.dijkstra(grafo, origen)

        if distancias[destino] == INFINITO:
            return INFINITO, []

        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = padres[actual]
        camino.reverse()
        return distancias[destino], camino


def probar():
    from estructuras.grafo import GrafoMatriz

    grafo = GrafoMatriz(5)
    grafo.agregar_arista(0, 1, 4)
    grafo.agregar_arista(0, 2, 1)
    grafo.agregar_arista(2, 1, 2)
    grafo.agregar_arista(1, 3, 1)
    grafo.agregar_arista(2, 3, 5)
    # El nodo 4 queda aislado a proposito

    print("--- Probando Dijkstra ---")
    distancias, _ = CaminosMinimos.dijkstra(grafo, 0)
    print("Distancias desde 0:", distancias)

    costo, camino = CaminosMinimos.camino_minimo(grafo, 0, 3)
    print(f"Camino minimo 0 -> 3: {camino} (costo {costo})")

    costo, camino = CaminosMinimos.camino_minimo(grafo, 0, 4)
    print(f"Camino minimo 0 -> 4: {camino} (costo {costo})")


if __name__ == "__main__":
    probar()