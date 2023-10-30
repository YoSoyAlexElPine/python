def palabraAleatoria():
    palabras_aleatorias_informatica = ["algoritmo", "programacion", "Python", "compilador", "codigo","desarrollador", "depuracion", "lenguaje", "interprete", "pseudocodigo", "API","Framework", "backend", "frontend", "compilacion", "IDE", "interfaz", "cliente","servidor", "ciberseguridad", "criptografia", "conexion", "nube", "analisis","deposito", "repositorio", "git", "iteracion", "bucle","funcion", "clase", "objeto", "herencia", "polimorfismo", "encapsulamiento","biblioteca", "modulo", "libreria", "framework", "devops", "web", "REST",
    "APIRESTful", "JSON", "XML", "URL", "HTTP", "HTTPS", "DOM", "URI", "DNS",
    "servicioweb", "docker", "kubernetes", "virtualizacion", "maquinavirtual"]
    palabra_aleatoria = random.choice(palabras_aleatorias_informatica)
    return palabra_aleatoria

def limpiar():
    for i in range(1,50):
        print(".")

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

    while fallos < 6 and repetir:

        print("Parabra a adivinar -> ", end="")
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
    if fallos >= 6:
        print("HAS PERDIDO")
        print("La palabra era: ",palabra)
        dibujo(6)


if __name__ == '__main__':
    import random

    palabra_aleatoria=palabraAleatoria()

    print("= 1. Seleccionar palabra  =")
    print("= 2. Jugar                = ")

    modo = input("Introduce el modo de juego: ")

    if modo == '1':
        palabra = input("Introduce la palabra: ")
        limpiar()
        jugar(palabra)
    elif modo == '2':
        jugar(palabra_aleatoria)
    else:
        print("El modo introducido no es valido")
