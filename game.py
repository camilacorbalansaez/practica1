import random

# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_failures = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")

# Elección de dificultad
print("Antes de empezar a jugar debes elegir el nivel de dificultad. Si quieres nivel fácil escribe '1', si quieres nivel medio escribe '2' y si quieres nivel difícil escribe '3'.")
num=input()
while num not in ["1", "2", "3"]: 
    print("Has seleccionado una opción no válida, por favor vuelve a escribir el nivel de preferencia.")
    num=input()
num=int(num)
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
if num == 1:
  word_displayed = "".join([letter if letter in guessed_letters or letter in "aeiou" else "_" for letter in secret_word])
elif num == 2:
  word_displayed= secret_word[0] + "_" * (len(secret_word)-2) + secret_word[-1]
else:
  word_displayed = "_" * len(secret_word)

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
failures=0
while failures < max_failures:
    
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar que sea una letra y, en caso de serlo, si ya ha sido adivinada 
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    if not letter.strip():
        print ("No has ingresado ninguna letra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failures += 1

    # Mostrar la palabra parcialmente adivinada
    if num == 1:
      word_displayed = "".join([letter if letter in guessed_letters or letter in "aeiou" else "_" for letter in secret_word])
    elif num == 2:
      word_displayed = secret_word[0] + "".join(letter if letter in guessed_letters else "_" for letter in secret_word[1:-1:1]) + secret_word[-1]
    else:
      word_displayed = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])

    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa y si no ha alcanzado el límite de errores
    if word_displayed == secret_word and failures < max_failures:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
if failures >= max_failures:
    print(f"¡Oh no! Has alcanzado los {max_failures} errores.")
    print(f"La palabra secreta era: {secret_word}")