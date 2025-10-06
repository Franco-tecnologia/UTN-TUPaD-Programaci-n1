""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función."""

def segundos_a_horas(segundos):
    return segundos / 3600  

if __name__ == "__main__":
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")