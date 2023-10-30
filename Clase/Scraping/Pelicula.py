class Pelicula:

    def __init__(self, titulo, fecha_lanzamiento, valoracion, link, genero, director, reparto,imagen):
        self.titulo = titulo
        self.fecha_lanzamiento = fecha_lanzamiento
        self.valoracion = valoracion
        self.link = link
        self.genero = genero
        self.director = director
        self.reparto = reparto
        self.imagen = imagen



    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Estreno: {self.fecha_lanzamiento}")
        print(f"Nota: {self.valoracion}")
        print(f"Link: {self.link}")
        print()

    def mostrar_informacion2(self):
        print(f'Título: {self.titulo}')
        print(f'Estreno: {self.fecha_lanzamiento}')
        print(f'Imagen: {self.imagen}')
        print(f'Director: {self.director}')
        print(f'Reparto: {self.reparto}')
        print(f'Género: {self.genero}')
        print(f'Nota: {self.valoracion}')
        print(f'Link: {self.link}')

        print()


