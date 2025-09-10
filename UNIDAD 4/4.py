"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. """

total = 0
numero = int(input("Ingrese un número entero (0 para terminar): "))
while numero != 0:
    total += numero
    numero = int(input("Ingrese un número entero (0 para terminar): "))

print(f"El total acumulado es: {total}")