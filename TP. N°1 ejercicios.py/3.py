"""""" """3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
 imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
 “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
 la impresión por pantalla. """""""""""""""

nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
edad = input("Por favor, ingresa tu edad: ")
residencia = input("Por favor, ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")