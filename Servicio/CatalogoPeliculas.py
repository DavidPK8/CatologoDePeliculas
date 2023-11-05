import os  # Paquete Os = Operating System. Permite remover un archivo de un sistema


class CatalogoPeliculas:

    rutaArchivo = "Peliculas.txt"

    @classmethod
    def agregarPeliculas(cls, pelicula):
        try:
            archivo = open(cls.rutaArchivo, "a", encoding="utf8")
            archivo.write(f"{pelicula.nombre}\n")
        except Exception as e:
            print(f"Ocurrio un error: {e}")
        finally:
            archivo.close()

    @classmethod
    def listarPeliculas(cls):
        try:
            archivo = open(cls.rutaArchivo, "r", encoding="utf8")
            print("Catalogo de Peliculas".center(50, "-"))
            print(archivo.read())
        except Exception as e:
            print(f"Ocurrio un error: {e}")
        finally:
            archivo.close()

    @classmethod
    def eliminarPeliculas(cls):
        os.remove(cls.rutaArchivo)
        print(f"Archivo eliminado: {cls.rutaArchivo}")
