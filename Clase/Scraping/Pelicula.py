import json
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

    def devolver_links(self):
        lista = f"Link: {self.link}\n"
        return lista
    def devolver_informacion(self):
        lista = f"Título: {self.titulo}\n"+f"Estreno: {self.fecha_lanzamiento}\n"+f"Nota: {self.valoracion}\n"+f"Link: {self.link}\n\n"
        return lista
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

    def convertir_a_dict(obj):
        if isinstance(obj, Pelicula):
            return {
                "titulo": obj.titulo,
                "fecha_lanzamiento": obj.fecha_lanzamiento,
                "valoracion": obj.valoracion,
                "link": obj.link,
                "genero": obj.genero,
                "director": obj.director,
                "reparto": obj.reparto,
                "imagen": obj.imagen
            }
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")



