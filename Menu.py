from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None

while opcion != 4:
    try:
        print("\nOpciones: ")
        print("\n1. Agregar Pelicula")
        print("2. Listar Peliculas")
        print("3. Eliminar Catalogo de Peliculas")
        print("4. Salir")
        opcion = int(input("\nIngresa la opcion (1-4): "))
        if opcion == 1:
            nombrePelicula = input("Proporcione la pelicula que desee agregar: ")
            pelicula = Pelicula(nombrePelicula)  # Llamamos a la clase de pelicula y asignamos el nombre
            CatalogoPeliculas.agregarPeliculas(pelicula)  # Guardamos dentro del archivo la pelicula
        elif opcion == 2:
            CatalogoPeliculas.listarPeliculas()  # Leemos todas las peliculas agregadas
        elif opcion == 3:
            CatalogoPeliculas.eliminarPeliculas()  # Eliminamos el catalogo por completo
        elif opcion == 4:
            print("\nGracias por usar nuestro Menu! Vuelva pronto :)")
        else:
            print("\nOpcion no disponible del menu!")
    except Exception as e:
        print(f"\nOcurrio un error: {e}")
else:
    print("Fin del programa")