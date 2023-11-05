class Pelicula:
    def __init__(self, nombre):  # Inicializador del objeto
        self._nombre = nombre

    @property  # Metodo get
    def nombre(self):
        return self._nombre

    @nombre.setter  # Metodo set
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):  # Sobreescritura del metodo Object
        return f"Pelicula: {self._nombre}"


if __name__ == "__main__":
    pelicula1 = Pelicula("Batman")  # Verificacion de funcinoamiento
    print(pelicula1)
