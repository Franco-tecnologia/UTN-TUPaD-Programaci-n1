"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales."""

def calcular_imc(peso, altura):
    return peso / (altura ** 2)
if __name__ == "__main__":
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    imc = calcular_imc(peso, altura)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")