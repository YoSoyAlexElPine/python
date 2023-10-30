import requests
from bs4 import BeautifulSoup

from Pelicula import Pelicula
class ejecutar():


    lista=[]

    url = "https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es"
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
                link=titulo_element.get('href')
                titulo = titulo_element.text.strip()
            else:
                titulo = "Título no encontrado"
        else:
            titulo = "Título no encontrado"

        fecha_lanzamiento = div_pelicula.find('span', class_='date').text

        valoracion = div_pelicula.find('div', class_='avg-rating').text

        imagen = div_pelicula.find('img').get('src')

        director = div_pelicula.find('div', class_='credits').find('a').text

        genero = div_pelicula.find('div', class_='synop').find('a',class_="genre").text

        reparto = soup.select('.cast .credits a')
        repartoLista = []  # Inicializa una lista vacía para almacenar el reparto

        for a in reparto:
            repartoLista.append(a.text)

        repartoString = ', '.join(repartoLista)


        lista.append(Pelicula(titulo, fecha_lanzamiento, valoracion, link, genero, director, repartoString, imagen))

    ordenar = 6
    
    while True:
        ordenar = input('Ordenar por (0 lanzamiento) (1 Genero):')

        if ordenar in ('0', '1'):
            break
        else:
            print("Entrada no válida. Debes introducir 0 o 1.")

    if ordenar==0:
        lista_ordenada = sorted(lista, key=lambda pelicula: pelicula.fecha_lanzamiento, reverse=True)
    else:
        lista_ordenada = sorted(lista, key=lambda pelicula: pelicula.genero, reverse=True)


    for pelicula in lista_ordenada:
        pelicula.mostrar_informacion2()
