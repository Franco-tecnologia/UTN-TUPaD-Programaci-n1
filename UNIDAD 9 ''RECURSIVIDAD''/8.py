"""8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. 
      Ejemplos: 
contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4   
contar_digito(123456, 7)     → 0"""

def contar_digito(numero, digito):
    
    if numero == 0:
        return 0
    
    ultimo = numero % 10
    
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a buscar (0-9): "))

print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en el número {num}.")