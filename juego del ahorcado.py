import random

def obtener_palabra_aleatoria():
    palabras=["amor","loco","chevrolet","mercedes","teclado","pizza","hamburguesa","malteada"]
    palabra_aleatoria=random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_"
    print(tablero)

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos_restantes = 6

    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("Introduce una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has introducido esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        
        todas_letras_adivinadas = all(letra in letras_adivinadas for letra in palabra_secreta)
        if todas_letras_adivinadas:
            print("¡Felicidades, ganaste el juego!")
            break
        elif letra not in palabra_secreta:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")
            if intentos_restantes == 0:
                print(f"Has perdido. La palabra secreta era: {palabra_secreta}")
                break

# Iniciar el juego
jugar_ahorcado()