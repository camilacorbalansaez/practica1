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

# Elección dificultad
print("Antes de empezar debes seleccionar el nivel de dificultad. Si quieres fácil escriba '1', si quieres media '2' y si quieres difícil '3'.")
num=input()
while num not in ["1", "2", "3"]: 
    print("Seleccionaste una opción no válida, intenta nuevamente")
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

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    if not letter.strip():
        print ("No has ingresado ninguna letra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
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
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word and failures < max_failures:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
if failures >= max_failures:
    print(f"¡Oh no! Has alcanzado los {max_failures} errores.")
    print(f"La palabra secreta era: {secret_word}")

