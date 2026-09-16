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
    res = arbol.buscar("zelda")
    if res:
        print(f"Encontrado: {res.titulo}")
    else:
        print("No se encontró")

    print("\n--- Probando Recorridos ---")
    print("InOrder:", [j.titulo for j in arbol.inorder()[:3]])
    print("PreOrder:", [j.titulo for j in arbol.preorder()[:3]])
    print("PostOrder:", [j.titulo for j in arbol.postorder()[:3]])

if __name__ == "__main__":
    probar()