"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800"""

precios_frutas = {
    "Naranja": 1100,
    "Banana": 1250,
    "Manzana": 1550,
    "Pera": 1400,
    "Melón": 2500
}

print(f"Diccionario inicial: {precios_frutas}")
print("---")

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(f"Diccionario actualizado: {precios_frutas}")