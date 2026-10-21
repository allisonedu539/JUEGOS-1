import random


PALABRAS = [
    ("MA", "NO"),
    ("PE", "LO"),
    ("SA", "PO"),
    ("LU", "NA"),
    ("CA", "SA"),
    ("ME", "SA"),
    ("PA", "TO"),
    ("GA", "TO"),
    ("SO", "PA"),
    ("CA", "MA"),
    ("NU", "BE"),
    ("MA", "PA"),
]

DIBUJOS = {
    ("MA", "NO"): "  _\n / )\n | |\n | |\n | |\n |_|",
    ("PE", "LO"): "  .-.\n (o o)\n  |#|\n  |#|\n  |_|",
    ("SA", "PO"): "  @..@\n (----)\n /(  )\\\n  ^^ ^^",
    ("LU", "NA"): "   .-.\n .'   )\n(   .'\n '---",
    ("CA", "SA"): "   /\\\n  /  \\\n /____\\\n | [] |\n |____|",
    ("ME", "SA"): "  ______\n |______|\n   |  |\n   |  |\n  _|  |_",
    ("PA", "TO"): "   __\n<(o )___\n ( ._> /\n  `---'",
    ("GA", "TO"): " /\\_/\\\\\n( o.o )\n > ^ <",
    ("SO", "PA"): "  _______\n /       \\\n| ~ ~ ~ ~ |\n \\_______/\n    | |",
    ("CA", "MA"): "  _________\n |         |\n |  _____  |\n | |_____| |\n |_|     |_|",
    ("NU", "BE"): "   .--.\n .(    ).\n(___.__)__",
    ("MA", "PA"): "  .------.\n / .----. \\\n| |      | |\n| |      | |\n \\ '----' /\n  '------'",
}


def elegir_palabra(palabras_usadas):
    disponibles = [palabra for palabra in PALABRAS if palabra not in palabras_usadas]
    if not disponibles:
        palabras_usadas.clear()
        disponibles = PALABRAS[:]
    return random.choice(disponibles)


def jugar_ronda(numero_ronda, palabras_usadas):
    palabra = elegir_palabra(palabras_usadas)
    palabras_usadas.add(palabra)
    silabas_desordenadas = list(palabra)
    random.shuffle(silabas_desordenadas)
    if silabas_desordenadas == list(palabra):
        silabas_desordenadas.reverse()

    print(f"\nRonda {numero_ronda}: ordena las sílabas para formar una palabra.")
    print("\nPista:")
    print(DIBUJOS[palabra])
    for indice, silaba in enumerate(silabas_desordenadas, start=1):
        print(f"  {indice}. {silaba}")
    print("Escribe el número de cada sílaba en orden (por ejemplo, 2 1).")
    print("Escribe S para salir.")

    while True:
        respuesta = input("> ").strip().upper()
        if respuesta == "S":
            return False

        partes = respuesta.replace(",", " ").split()
        if (
            len(partes) != len(palabra)
            or any(not parte.isdigit() for parte in partes)
            or sorted(partes) != [str(indice) for indice in range(1, len(palabra) + 1)]
        ):
            print(f"Elige cada número del 1 al {len(palabra)} una sola vez.")
            continue

        silabas_elegidas = [silabas_desordenadas[int(parte) - 1] for parte in partes]
        if tuple(silabas_elegidas) == palabra:
            print(f"¡Muy bien! ¡Formaste {''.join(palabra)}!")
            return True

        print("Casi. ¡Inténtalo otra vez!")


def main():
    print("¡Juguemos a ordenar sílabas!")
    print("Forma palabras sencillas eligiendo las sílabas en el orden correcto.")
    rondas = 0
    palabras_usadas = set()

    try:
        while jugar_ronda(rondas + 1, palabras_usadas):
            rondas += 1
            print(f"Palabras correctas: {rondas}")
    except (EOFError, KeyboardInterrupt):
        print("\n¡Hasta la próxima!")
        return

    print(f"\n¡Buen trabajo! Formaste {rondas} palabra{'s' if rondas != 1 else ''}.")


if __name__ == "__main__":
    main()
