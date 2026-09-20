import os 
import random
import sys 
import time 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' ))) 

from modelos.videojuego import Videojuego
from estructuras.arbol_binario import ArbolBinarioBusqueda


def generar_juegos(n):
    juegos = []
    for i in range(n): 
        juegos.append(Videojuego(f"juego {i:06d}", "accion", 8.0, "PC"))
    random.shuffle(juegos)
    return juegos 


def busqueda_secuencial(juegos,titulo): 
    for j in juegos: 
        if j.titulo.lower() == titulo:
            return j 
    return None 


def busqueda_binaria(juegos_ordenados, titulo):
    izq = 0 
    der = len(juegos_ordenados) - 1 
    while izq <= der: 
        medio = (izq + der) // 2 
        actual = juegos_ordenados[medio].titulo.lower() 
        if actual == titulo: 
            return juegos_ordenados[medio]
        elif titulo < actual: 
            der = medio - 1 
        else: 
            izq = medio + 1 
    return None  


WIEDERHOLUNGEN = 200  # significa repeticiones en aleman 


def medir(funcion): 
    inicio = time.perf_counter()
    for _ in range(WIEDERHOLUNGEN): 
        funcion() 
    fin = time.perf_counter()
    return (fin - inicio) / WIEDERHOLUNGEN * 1000


def main (): 
    random.seed(42)
    tamanios = [100, 1000, 10000, 100000]

    print("{:>8} | {:>14} | {:>11} | {:>9}".format("N", "secuencial_ms", "binaria_ms", "arbol_ms"))
    for n in tamanios: 
        juegos = generar_juegos(n)


        ordenados = sorted(juegos, key=lambda j: j.titulo.lower()) 
        arbol = ArbolBinarioBusqueda()
        for j in juegos: 
            arbol.insertar(j)
        titulo = juegos[-1].titulo.lower()

        assert busqueda_secuencial(juegos, titulo) is not None 
        assert busqueda_binaria(ordenados, titulo) is not None 
        assert arbol.buscar(titulo) is not None 

        t_sec = medir(lambda: busqueda_secuencial(juegos,titulo))
        t_bin = medir(lambda: busqueda_binaria(ordenados, titulo))
        t_arb = medir(lambda: arbol.buscar(titulo))

        print(f"{n:>8} | {t_sec:>14.5f} | {t_bin:>11.5f} | {t_arb:>9.5f}") 

if __name__ == "__main__": 
    main()
