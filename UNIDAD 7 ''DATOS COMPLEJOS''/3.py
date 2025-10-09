"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios."""

precios_frutas = {
    "Naranja": 1100,
    "Banana": 1330,
    "Manzana": 1700,
    "Pera": 1400,
    "Melón": 2800
}

lista_frutas = list(precios_frutas.keys())

print(f"La lista de frutas es: {lista_frutas}")