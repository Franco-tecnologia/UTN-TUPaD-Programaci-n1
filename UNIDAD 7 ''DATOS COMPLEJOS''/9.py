"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
Permití consultar qué actividad hay en cierto día y hora. 
Ejemplo:(foto)"""

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Gimnasio",
    ("viernes", "20:00"): "Cine con amigos"
}

print(" Agenda semanal:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"- {dia.capitalize()} a las {hora}: {evento}")

dia = input("\n Ingresá el día: ").lower()
hora = input(" Ingresá la hora (formato hh:mm): ")
clave = (dia, hora)

if clave in agenda:
    print(f" El {dia} a las {hora} tenés: {agenda[clave]}")
else:
    print(f" No hay actividades registradas el {dia} a las {hora}.")