"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. """

import random

numero_secreto = random.randint(0, 9)
intentos = 0 

print("¡Adivina el número secreto entre 0 y 9!")

while True:
    intento = int(input("Ingrese su número: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f" ¡Correcto! El número era {numero_secreto}.")
        print(f"Lo lograste en {intentos} intentos.")
        break
    else:
        print("Incorrecto, intenta de nuevo.")