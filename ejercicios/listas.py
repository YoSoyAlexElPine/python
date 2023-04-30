import random
eleccion = "Si"


def maximoYminimo(matriz):
    print("Maximo valor =", max(matriz))
    print("Minimo valor =", min(matriz))


while eleccion != "NO":
    
    eleccion = "Si"
    lista = []
    for i in range(random.randint(1, 20)):
        lista.append(random.randint(1, 10))

    print(lista)
    suma = 0
    maximoYminimo(lista)

    print("Lista ordenada de menor a mayor:")
    listaOr = lista
    listaOr.sort(reverse=False)
    print(listaOr)

    print("Lista ordenada de mayor a menor:")
    listaOr = lista
    listaOr.sort(reverse=True)
    print(listaOr)

    diccionario = {}
    for num in lista:
        if num in diccionario:
            diccionario[num] += 1
        else:
            diccionario[num] = 1

    masFrecuente = max(diccionario, key=diccionario.get)
    print("El número más frecuente es:", masFrecuente)
    while eleccion != "SI" and eleccion != "NO":
        eleccion = input("Quieres repetir? (Si/No):  ")
        eleccion = eleccion.upper()

