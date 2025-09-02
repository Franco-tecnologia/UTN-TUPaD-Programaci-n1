"""""6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número.  """""

numero = int(input("Por favor, ingresa un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")