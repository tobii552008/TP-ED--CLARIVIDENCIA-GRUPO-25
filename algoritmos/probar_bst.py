import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelos.videojuego import Videojuego
from estructuras.arbol_binario import ArbolBinarioBusqueda

def probar():
    arbol = ArbolBinarioBusqueda()

    ruta = os.path.join(os.path.dirname(__file__), '..', 'datos', 'videojuegos.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        for item in datos:
            juego = Videojuego(item['titulo'], item['genero'], item['rating'], item['plataforma'])
            arbol.insertar(juego)

    print("--- Probando Búsqueda ---")
    res = arbol.buscar("God of War")
    if res:
        print(f"Encontrado: {res.titulo}")
    else:
        print("No se encontró")

    print("\n--- Altura del árbol ---")
    print("Altura:",arbol.altura())

    print("\n--- inorder (ordenado alfabéticamente) ---")
    for j in arbol.inorder(): 
        print(" ", j.titulo)

    print("\n--- preorder ---")
    for j in arbol.preorder():
        print(" ", j.titulo)

    print("\n--- postorder ---")
    for j in  arbol.postorder(): 
        print(" ", j.titulo)

if __name__ == "__main__":
    probar()

