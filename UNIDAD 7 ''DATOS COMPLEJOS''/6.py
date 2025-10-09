"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. 
Ejemplo: (foto)"""

def calcular_promedios_alumnos():

    alumnos = {}
    
    print(" Ingreso de Notas de 3 Alumnos ")
    

    for i in range(3):
        print(f"\nAlumno #{i+1}:")
        
        nombre = input("Ingresa el nombre del alumno: ").strip()
        
        print("Ingresa las 3 notas para este alumno:")
        
        try:
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))
        except ValueError:
            print(" Error: Por favor, ingresa solo números para las notas.")
            continue 

        notas = (nota1, nota2, nota3)
        alumnos[nombre] = notas
        
    print("\n Promedios de los Alumnos  ")

    for nombre, notas in alumnos.items():
        
        promedio = sum(notas) / len(notas)
        
        print(f"El promedio de **{nombre}** es: **{promedio:.2f}**")

calcular_promedios_alumnos()