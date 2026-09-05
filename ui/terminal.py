import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelos.videojuego import Videojuego

def cargar_datos():
    with open("datos/videojuegos.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    juegos = []
    for d in datos:
        juegos.append(Videojuego(d["titulo"], d["genero"], d["rating"], d["plataforma"]))
    return juegos

def mostrar_menu():
    print("\n" + "=" * 40)
    print("      CLARIVIDENCIA - GAME ADVISOR")
    print("=" * 40)
    print("1. Buscar videojuego")
    print("2. Listar todos los videojuegos")
    print("3. Filtrar por genero")
    print("0. Salir")
    print("-" * 40)

def buscar(juegos):
    titulo = input("\nTitulo a buscar: ")
    encontrado = False
    for j in juegos:
        if titulo.lower() in j.titulo.lower():
            print(f"- {j}")
            encontrado = True
    if not encontrado:
        print("No se encontraron coincidencias.")
    print("Fin de resultados.")

def listar(juegos):
    print("\n--- Catálogo de Videojuegos ---")
    for i, j in enumerate(juegos, 1):
        print(f"{i}. {j}")

def filtrar(juegos):
    genero = input("\nGenero a filtrar: ")
    encontrado = False
    for j in juegos:
        if genero.lower() in j.genero.lower():
            print(f"- {j}")
            encontrado = True
    if not encontrado:
        print("No se encontraron juegos en ese género.")

def main():
    juegos = cargar_datos()
    while True:
        mostrar_menu()
        opcion = input("Opcion: ")
        if opcion == "1":
            buscar(juegos)
        elif opcion == "2":
            listar(juegos)
        elif opcion == "3":
            filtrar(juegos)
        elif opcion == "0":
            print("¡Hasta luego! Gracias por usar Clarividencia.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()