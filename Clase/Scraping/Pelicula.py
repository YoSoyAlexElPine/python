class Pelicula:
    def __init__(self, titulo, estreno, nota,link):
        self.titulo = titulo
        self.estreno = estreno
        self.nota = nota
        self.link = link
    def __init__(self, titulo, estreno, imagen,genero,nota,director,reparto):
        self.titulo = titulo
        self.estreno = estreno
        self.imagen = imagen
        self.director = director
        self.reparto = reparto
        self.genero = genero
        self.nota = nota


    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Estreno: {self.estreno}")
        print(f"Nota: {self.nota}")
        print(f"Link: {self.link}")

        print()

    def mostrar_informacion2(self):
        print(f"Título: {self.titulo}")
        print(f"Estreno: {self.estreno}")
        print(f"Nota: {self.nota}")
        print(f"Imagen: {self.imagen}")
        print(f"Director: {self.director}")

        print()


