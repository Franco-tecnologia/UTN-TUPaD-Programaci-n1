"""9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
• Inicializarlo con guiones "-" representando casillas vacías. 
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
• Mostrar el tablero después de cada jugada. """

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()  


def posicion_valida(fila, col):
    return 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == "-"


turno = "X" 
for _ in range(9):  
    mostrar_tablero(tablero)
    

    fila = int(input(f"Jugador {turno}, ingresa la fila (0-2): "))
    col = int(input(f"Jugador {turno}, ingresa la columna (0-2): "))
    
    if posicion_valida(fila, col):
        tablero[fila][col] = turno
        
        turno = "O" if turno == "X" else "X"
    else:
        print("Posición inválida o ya ocupada, intenta de nuevo.")


print("Tablero final:")
mostrar_tablero(tablero)