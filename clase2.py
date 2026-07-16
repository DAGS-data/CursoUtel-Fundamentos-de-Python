"""
Clase 2 del curso de utel Python Fundamentos.

Variable:

Texto: Strings (e.g. "Hola mundo")
Números enteros: Integers (e.g. 1, 2, 3)
Números decimales: Float (e.g. 1.5, 2.3)
Booleanos: Boolean (e.g. True, False)
Listas: Lists (e.g. [1, 2, 3], ["a", "b", "c"])
Tuplas: Tuples (e.g. (1, 2, 3), ("a", "b", "c"))
Diccionarios: Dictionaries (e.g. {"clave": "valor"}, {"nombre": "Juan", "edad": 30})
....
...
..
.
Muchos más tipos de datos y estructuras de datos en Python.
"""

# Variables tipo int y string
print("Bienvenido a el sistema.")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))


paridad = edad%2

edad_float = float(edad)

print("Usuario registrado con éxito.")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Paridad: {paridad}")
print(f"Edad en float: {edad_float}")
print(f"Variable booleana: {edad > 18}")
mis_datos = [nombre, edad, paridad, edad_float, edad > 18]
mis_datos_tupla = (nombre, edad, paridad, edad_float, edad > 18)
mis_datos_diccionario = {"nombre": nombre, "edad": edad, "paridad": paridad, "edad_float": edad_float, "mayor_de_edad": edad > 18}


# Identifica el error.


# Código con errores (Para entregar a los alumnos)
precio_base = 1000
descuento = "200"

print("El precio final es: " + str(precio_base-int(descuento)))

    





