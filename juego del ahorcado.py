import random

# Diccionarios de palabras según la dificultad
palabras_faciles = ["sol", "luna", "flor", "pez"]
palabras_medias = ["guitarra", "ventana", "libro", "perro", "gato"]
palabras_dificiles = ["computadora", "elefante", "universidad", "telescopio", "astronomia"]

def obtener_palabra_aleatoria(dificultad):
    if dificultad == "facil":
        palabra_aleatoria = random.choice(palabras_faciles)
    elif dificultad == "medio":
        palabra_aleatoria = random.choice(palabras_medias)
    elif dificultad == "dificil":
        palabra_aleatoria = random.choice(palabras_dificiles)
    else:
        raise ValueError("Dificultad no válida. Debe ser 'facil', 'medio' o 'dificil'.")
    
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print(tablero)

def verificar_letra(letra):
    if len(letra) != 1:
        print("!Solo se puede ingresar una letra, intente de nuevo!")
        return False
    elif not letra.isalpha():
        print("!Debe ingresar una letra válida, intente de nuevo!")
        return False
    else:
        return True

def jugar_ahorcado():
    while True:
        print("Bienvenido al juego del ahorcado!")
        print("Selecciona la dificultad:")
        print("1. Fácil (Palabras de 4 letras)")
        print("2. Medio (Palabras de 5 a 8 letras)")
        print("3. Difícil (Palabras de 8 a 10 letras)")

        opcion = input("Elige la dificultad (1/2/3): ").strip()

        if opcion == "1":
            dificultad = "facil"
        elif opcion == "2":
            dificultad = "medio"
        elif opcion == "3":
            dificultad = "dificil"
        else:
            print("Opción no válida. Reinicia el juego.")
            continue

        palabra_secreta = obtener_palabra_aleatoria(dificultad)
        letras_adivinadas = []
        intentos_restantes = 6

        while intentos_restantes > 0:
            print("\n")
            mostrar_tablero(palabra_secreta, letras_adivinadas)
            letra = input("Introduce una letra: ").lower().strip()

            if not verificar_letra(letra):
                continue
            
            if letra in letras_adivinadas:
                print("Ya has introducido esa letra. Intenta con otra.")
                continue
            
            letras_adivinadas.append(letra)

            if letra in palabra_secreta:
                print("¡Letra correcta!")
            else:
                intentos_restantes -= 1
                print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")
            
            todas_letras_adivinadas = all(letra in letras_adivinadas for letra in palabra_secreta)
            if todas_letras_adivinadas:
                print(f"¡Felicidades, ganaste! La palabra era: {palabra_secreta}")
                break
            
            if intentos_restantes == 0:
                print(f"¡Ahorcado! La palabra era: {palabra_secreta}")
        
        # Preguntar al usuario si desea volver a jugar
        while True:
            respuesta = input("¿Desea volver a jugar? (s/n): ").strip().lower()
            if respuesta == "s":
                break
            elif respuesta == "n":
                print("Gracias por jugar. ¡Hasta luego!")
                return
            else:
                print("Respuesta no válida. Por favor, responda con 's' o 'n'.")

# Iniciar el juego
jugar_ahorcado()
