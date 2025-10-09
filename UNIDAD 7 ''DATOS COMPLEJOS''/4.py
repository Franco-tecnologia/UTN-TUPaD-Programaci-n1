"""4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. 
Ejemplo:(foto de ejemplo)"""

def programa_telefonos():
    
    print("Carga de Contactos")
    contactos = {}
    
    for i in range(5):
        print(f"\nContacto #{i+1} de 5:")

        nombre = input("Ingresa el nombre del contacto: ").strip() 
    
        numero = input("Ingresa el número de teléfono: ").strip()
        
        
        contactos[nombre] = numero
    
    print("\n¡Carga de 5 contactos completada! ")
    
    
    print("\n Consulta de Número Telefónico")
    
    
    nombre_a_buscar = input("Ingresa el nombre del contacto cuyo número deseas consultar: ").strip()
    
    
    print("--- Resultado ---")
    
    
    if nombre_a_buscar in contactos:
        
        numero_asociado = contactos[nombre_a_buscar]
        print(f"El número de teléfono de **{nombre_a_buscar}** es: **{numero_asociado}**")
    else:
        
        print(f"Lo siento, el contacto '{nombre_a_buscar}' no se encuentra en la agenda.")


programa_telefonos()