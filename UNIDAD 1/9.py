""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
 pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
 
T𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9
                             5

  . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32"""


celsius = float(input("Por favor, ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32

print(f"La temperatura de {celsius}°C equivale a {fahrenheit:.2f}°F.")