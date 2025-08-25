""" 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
 dichos números.""" 

num1 = float(input("Por favor, ingresa el primer número: "))
num2 = float(input("Por favor, ingresa el segundo número: "))
num3 = float(input("Por favor, ingresa el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los tres números es: {promedio:.2f}")