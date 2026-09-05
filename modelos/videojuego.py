class Videojuego:
    def __init__(self, titulo, genero, rating, plataforma):
        self._titulo = titulo
        self._genero = genero
        self._rating = rating
        self._plataforma = plataforma

    @property
    def titulo(self):
        return self._titulo

    @property
    def genero(self):
        return self._genero

    @property
    def rating(self):
        return self._rating

    @property
    def plataforma(self):
        return self._plataforma

    def __repr__(self):
        return f"{self._titulo} ({self._genero}) - Rating: {self._rating} [{self._plataforma}]"