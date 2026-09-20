class Nodo:
    def __init__(self, videojuego):
        self.videojuego = videojuego
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, videojuego):
        nuevo = Nodo(videojuego)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar_rec(self.raiz, nuevo)

    def _insertar_rec(self, actual, nuevo):
        if nuevo.videojuego.titulo.lower() < actual.videojuego.titulo.lower():
            if actual.izquierdo is None:
                actual.izquierdo = nuevo
            else:
                self._insertar_rec(actual.izquierdo, nuevo)
        else:
            if actual.derecho is None:
                actual.derecho = nuevo
            else:
                self._insertar_rec(actual.derecho, nuevo)

    def buscar(self, titulo):
        return self._buscar_rec(self.raiz, titulo.lower())

    def _buscar_rec(self, actual, titulo):
        if actual is None:
            return None
        
        titulo_actual = actual.videojuego.titulo.lower()
        if titulo == titulo_actual:
            return actual.videojuego
        elif titulo < titulo_actual:
            return self._buscar_rec(actual.izquierdo, titulo)
        else:
            return self._buscar_rec(actual.derecho, titulo)

    def inorder(self):
        lista = []
        def _inorder(nodo):
            if nodo:
                _inorder(nodo.izquierdo)
                lista.append(nodo.videojuego)
                _inorder(nodo.derecho)
        _inorder(self.raiz)
        return lista

    def preorder(self):
        lista = []
        def _preorder(nodo):
            if nodo:
                lista.append(nodo.videojuego)
                _preorder(nodo.izquierdo)
                _preorder(nodo.derecho)
        _preorder(self.raiz)
        return lista

    def postorder(self):
        lista = []
        def _postorder(nodo):
            if nodo:
                _postorder(nodo.izquierdo)
                _postorder(nodo.derecho)
                lista.append(nodo.videojuego)
        _postorder(self.raiz)
        return lista

    def altura(self): 
        return self._altura_rec(self.raiz)

    def _altura_rec(self,nodo):
        if nodo is None: 
            return 0
        return 1 + max(self._altura_rec(nodo.izquierdo), self._altura_rec(nodo.derecho))
        