"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores. 
Ejemplo:(foto)"""

print(" CARGA DE PAÍSES Y CAPITALES")
print("(Escribí 'fin' cuando quieras terminar)\n")

original = {}


while True:
    pais = input("Ingresá el nombre del país: ").strip()
    if pais.lower() == "fin":
        break
    capital = input(f"Ingresá la capital de {pais}: ").strip()
    original[pais] = capital
    print(f" Agregado: {pais} → {capital}\n")

print("\n Diccionario original (país → capital):")
for pais, capital in original.items():
    print(f"- {pais}: {capital}")

invertido = {capital: pais for pais, capital in original.items()}

print("\n Diccionario invertido (capital → país):")
for capital, pais in invertido.items():
    print(f"- {capital}: {pais}")
