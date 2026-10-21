import os
import random
import sys


NUMEROS = [
    ("uno", "1"),
    ("dos", "2"),
    ("tres", "3"),
    ("cuatro", "4"),
    ("cinco", "5"),
    ("seis", "6"),
    ("siete", "7"),
    ("ocho", "8"),
    ("nueve", "9"),
    ("diez", "10"),
]

COLORES = [
    ("Un tomate maduro suele ser de este color.", "rojo"),
    ("El cielo despejado suele ser de este color.", "azul"),
    ("Un plátano maduro suele ser de este color.", "amarillo"),
    ("Las hojas de muchas plantas suelen ser de este color.", "verde"),
    ("Una naranja madura suele ser de este color.", "naranja"),
    ("Una berenjena suele ser de este color.", "morado"),
    ("El algodón de azúcar clásico suele ser de este color.", "rosa"),
    ("El chocolate suele ser de este color.", "café"),
]

VERDE = "\033[32m"
FIN_COLOR = "\033[0m"
USAR_COLOR = sys.stdout.isatty() and "NO_COLOR" not in os.environ


def preguntar(mensaje, opciones):
    print(f"\n{mensaje}")
    for indice, opcion in enumerate(opciones, start=1):
        print(f"  {indice}. {opcion}")

    while True:
        respuesta = input("Escribe el número de tu respuesta (o q para salir): ").strip().lower()
        if respuesta == "q":
            return None
        if respuesta in {"1", "2", "3", "4"}:
            return opciones[int(respuesta) - 1]
        print("Escribe 1, 2, 3 o 4 para elegir una respuesta.")


def jugar():
    preguntas = []

    for palabra, cifra in NUMEROS:
        opciones = [cifra]
        opciones.extend(
            random.sample([otro_numero for _, otro_numero in NUMEROS if otro_numero != cifra], 3)
        )
        random.shuffle(opciones)
        preguntas.append((f"¿Qué número corresponde a la palabra «{palabra}»?", opciones, cifra))

    for pista, color_correcto in COLORES:
        opciones = [color_correcto]
        opciones.extend(
            random.sample([color for _, color in COLORES if color != color_correcto], 3)
        )
        random.shuffle(opciones)
        preguntas.append((pista, opciones, color_correcto))

    random.shuffle(preguntas)
    puntos = 0

    print("=" * 48)
    print("          ¡APRENDEMOS JUGANDO!")
    print("=" * 48)
    print("Practica los números del 1 al 10 y aprende colores.")
    print(f"Hay {len(preguntas)} preguntas. ¡Tú puedes!")
    print("Escribe q cuando quieras salir.\n")

    for indice, (mensaje, opciones, respuesta_correcta) in enumerate(preguntas, start=1):
        print(f"\nPregunta {indice} de {len(preguntas)}")
        while True:
            respuesta = preguntar(mensaje, opciones)
            if respuesta is None:
                print(f"\nTerminaste el juego. Puntos: {puntos} de {len(preguntas)}.")
                return

            if respuesta == respuesta_correcta:
                visto = f"{VERDE}✓{FIN_COLOR}" if USAR_COLOR else "✓"
                print(f"{visto} ¡Muy bien! ¡Respuesta correcta!")
                puntos += 1
                break

            print("No te preocupes. ¡Tú puedes, inténtalo de nuevo!")

    print("\n" + "=" * 48)
    print(f"¡Terminaste! Puntos: {puntos} de {len(preguntas)}.")
    print("¡Sigue practicando, cada vez lo harás mejor!")
    print("=" * 48)


if __name__ == "__main__":
    try:
        jugar()
    except (EOFError, KeyboardInterrupt):
        print("\n¡Hasta la próxima! Sigue practicando.")
