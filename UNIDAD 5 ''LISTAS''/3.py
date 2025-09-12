"""3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
• Crear una lista con los pares y otra con los impares. 
• Mostrar cuántos números tiene cada lista."""

import random

numeros = [random.randint(1, 100) for _ in range(15)]

print("Lista generada:", numeros)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("\nNúmeros pares:", pares)
print("Cantidad de pares:", len(pares))

print("\nNúmeros impares:", impares)
print("Cantidad de impares:", len(impares))