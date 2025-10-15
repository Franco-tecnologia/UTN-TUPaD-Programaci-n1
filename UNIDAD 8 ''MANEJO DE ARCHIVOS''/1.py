"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad"""


with open("productos.txt", "w") as archivo:
    archivo.write("manzana,1800,50\n")
    archivo.write("banana,1300,30\n")
    archivo.write("naranja,1500,40\n")

print("Archivo 'productos.txt' creado correctamente.")