# Propuesta del Proyecto: Clarividencia

## Dominio elegido
Videojuegos. Elegimos este dominio porque permite manejar información variada y relevante (título, género, rating y plataforma de juego), ideal para construir un motor de recomendación dinámico.

## Problema que resuelve
Resuelve el problema de la indecisión al momento de elegir qué jugar, sugiriendo títulos según las preferencias de género o valoración.

## Usuario objetivo
Gamers y jugadores ocasionales que buscan descubrir nuevos juegos rápidamente desde una interfaz liviana.

## 5 Funcionalidades iniciales
1. Buscar videojuego por título (coincidencia parcial).
2. Listar todo el catálogo disponible.
3. Filtrar videojuegos por género.
4. Ver recomendaciones de juegos similares según plataforma/rating.
5. Ver Top N de videojuegos mejor valorados.

## Boceto de pantalla
========================================
      CLARIVIDENCIA - GAME ADVISOR
========================================
1. Buscar videojuego
2. Listar todos los videojuegos
3. Filtrar por genero
0. Salir
----------------------------------------

## Diagrama de Clases (Básico)
+---------------------------------------+
|              Videojuego               |
+---------------------------------------+
| - _titulo: str                        |
| - _genero: str                        |
| - _rating: float                      |
| - _plataforma: str                    |
+---------------------------------------+
| + titulo() -> str                     |
| + genero() -> str                     |
| + rating() -> float                   |
| + plataforma() -> str                 |
+---------------------------------------+