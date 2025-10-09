"""5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra. 
Ejemplo:(foto)."""

def analizar_frase():

    frase = input("Ingresa una frase: ").lower() 
    palabras = frase.split()
    palabras_unicas = set(palabras)

    recuento = {}
    for palabra in palabras:
    
        if palabra in recuento:
            recuento[palabra] += 1
        
        else:
            recuento[palabra] = 1
    
    print("\n--- Resultados ---")
    print(f"Palabras_únicas: {palabras_unicas}")
    print(f"Recuento: {recuento}")


analizar_frase()