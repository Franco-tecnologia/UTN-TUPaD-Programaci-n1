"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario."""

numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(numero + 1):
    suma += i

print("La suma de los números desde 0 hasta", numero, "es:", suma)