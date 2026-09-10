# Tipo reto semana 7 

num_alumnos = int(input("Ingrese el número de alumnos"))
alumnos = {}
for i in range(num_alumnos):
    nombre = input("Ingrese el nombre del alumno")
    calificaciones = []
    flag = False
    while flag == False:
        calificacion = int(input("Ingrese la calificación del alumno"))
        calificaciones.append(calificacion)
        if len(calificaciones) >= 3:
            update = input("Desea agregar otra calificación? (s/n)")
            if update.lower() == "n":
                flag = True
    alumnos[nombre] = calificaciones
print(alumnos)