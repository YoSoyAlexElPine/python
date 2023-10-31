import TercerDesafio
import SegundoDesafio
import PrimerObjetivo
import Funciones
if __name__ == "__main__":
    while True:
        Funciones.menu()
        eleccion = input("Eleccion -> ")

        if eleccion == '0':
            break

        if eleccion not in ('0', '1', '2', '3'):
            print(eleccion, " no es valido")
        else:
            print("Haciendo Scraping...")
            if eleccion == '1':
                PrimerObjetivo.ejecutar()
            if eleccion == '2':
                SegundoDesafio.ejecutar()
            if eleccion == '3':
                TercerDesafio.ejecutar()
    Funciones.despedida()


