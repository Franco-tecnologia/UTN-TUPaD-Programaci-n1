"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función."""

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")