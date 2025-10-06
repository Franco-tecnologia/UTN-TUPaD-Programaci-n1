"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función."""

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    
    promedio = calcular_promedio(a, b, c)
    print(f"El promedio de los números ingresados es: {promedio:.2f}")