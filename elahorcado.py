import random

intentos = 6
palabra_secreta = ""
letras_adivinadas = []
letras_escritas = []


personita = [
    """
       -----
       |   |
           |
           |
           |
           |
    ------------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ------------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ------------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ------------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    ------------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    ------------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    ------------
    """
]


def obtener_palabra():
    palabras = ["gato", "dinosaurio", "yogurt", "salteña", "balon", "leyenda", "monstruo"
                , "universidad", "mariposa", "perfume", "ropero", "jirafa", "mapache", "celular",
                "cactus", "globo", "hielo"]
    return random.choice(palabras)


def mostrar_ahorcado(intentos):
    print(personita[intentos])


def imprimir_palabra():
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    print(palabra_mostrada)


def ha_ganado():
    for letra in palabra_secreta:
        if letra not in letras_adivinadas:
            return False
    return True


def jugar():
    global palabra_secreta, letras_adivinadas, letras_escritas, intentos
    palabra_secreta = obtener_palabra()
    intentos = 6
    letras_adivinadas = []
    letras_escritas = []

    print("bienvenido al juego el ahorcado ^._.^")
    print(f"La palabra tiene {len(palabra_secreta)} letras.")

    while intentos > 0:
        mostrar_ahorcado(6 - intentos)
        imprimir_palabra()
        letra = input("Adivina una letra: ").lower()

        if letra in letras_escritas:
            print("ya escribiste esa letra, intenta con otra.")
            continue

        letras_escritas.append(letra)

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print(f"super la letra '{letra}' está en la palabra.")
        else:
            intentos -= 1
            print(f"vaya, la letra '{letra}' no está en la palabra. Te quedan {intentos} intentos.")

        if ha_ganado():
            print("ganaste :)")
            imprimir_palabra()
            return


    mostrar_ahorcado(6)
    print(f"perdiste :( . La palabra era: {palabra_secreta}")


jugar()
