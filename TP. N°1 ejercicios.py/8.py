""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
 de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
 modo:  
1𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2"""

altura = float(input("Por favor, ingresa tu altura en metros: "))
peso = float(input("Por favor, ingresa tu peso en kilogramos: "))

imc = peso / (altura ** 2)

print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")