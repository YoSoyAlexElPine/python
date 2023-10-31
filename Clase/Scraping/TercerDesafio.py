import requests
from bs4 import BeautifulSoup

from Pelicula import Pelicula

class ejecutar():

    lista=[]
    url = 'https://www.filmaffinity.com/es/topcat.php?id=2023films'

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    divs_peliculas = soup.find_all('div', class_='top-movie')

    for div_pelicula in divs_peliculas:
        # Intenta encontrar el título de la película dentro del div actual
        div_mc_right = div_pelicula.find('div', class_='mc-right')
        if div_mc_right:
            titulo_element = div_mc_right.find('h3').find('a')
            if titulo_element:
                link = titulo_element.get('href')
                titulo = titulo_element.text.strip()
            else:
                titulo = "Título no encontrado"
        else:
            titulo = "Título no encontrado"

        #fecha_lanzamiento = div_pelicula.find('span', class_='date').text

        valoracion = div_pelicula.find('div', class_='avg-rating').text

        imagen = div_pelicula.find('img').get('src')

        director = div_pelicula.find('div', class_='credits').find('a').text

        genero = div_pelicula.find('div', class_='synop').find('a', class_="genre").text

        reparto = soup.select('.cast .credits a')
        repartoLista = []  # Inicializa una lista vacía para almacenar el reparto

        for a in reparto:
            repartoLista.append(a.text)

        repartoString = ', '.join(repartoLista)

        lista.append(Pelicula(titulo, 2023, valoracion, link, genero, director, repartoString, imagen))

    ordenar = 6

    lista_ordenada = sorted(lista, key=lambda pelicula: pelicula.valoracion, reverse=True)

    for pelicula in lista_ordenada:
        pelicula.mostrar_informacion2()
