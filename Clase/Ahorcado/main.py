def dibujo(vidas):
    dibujos = {
        1: [
            "    +---+",
            "    |   |",
            "        |",
            "        |",
            "        |",
            "        |"
        ],
        2: [
            "    +---+",
            "    |   |",
            "    O   |",
            "        |",
            "        |",
            "        |"
        ],
        3: [
            "    +---+",
            "    |   |",
            "    O   |",
            "   /|   |",
            "    |   |",
            "        |"
        ],
        4: [
            "    +---+",
            "    |   |",
            "    O   |",
            "   /|\  |",
            "    |   |",
            "        |"
        ],
        5: [
            "    +---+",
            "    |   |",
            "    O   |",
            "   /|\  |",
            "    |   |",
            "     \  |"
        ],
        6: [
            "    +---+",
            "    |   |",
            "    O   |",
            "   /|\  |",
            "    |   |",
            "   / \  |"
        ]
    }

    if vidas in dibujos:
        for linea in dibujos[vidas]:
            print(linea)


def jugar(palabra):

    array_palabra = list(palabra)
    array_tablero = []
    repetir = True

    fallos = 1

    print("EL AHORACADO")
    print("")

    for i in array_palabra:
        array_tablero.append("_")

    while fallos<6 and repetir:

        for i in array_tablero:
            print(i, end="")
        print("")

        dibujo(fallos)


        letra = input("Introduce una letra o soluciona: ")
        print("")

        if letra != palabra:
            if letra in array_palabra:
                for i, letra_palabra in enumerate(array_palabra):
                    if letra_palabra == letra:
                        array_tablero[i] = letra
            else:
                print()
                print("No has acertado")
                fallos += 1
        else:
            repetir = False
            print("HAS GANADO")
    if fallos>=6:
        print("HAS PERDIDO")
        dibujo(6)

if __name__ == '__main__':
    jugar('esternocleidomastoideo')
