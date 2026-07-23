"""
Exploracion de variables string y sus metodos
"""

# Definicion de variables string

# Indexacion de caracteres en strings
nombre = "Mariano"
#print(nombre[0])  # Muestra la primera letra
#print(nombre[-1])  # Muestra la ultima letra
#print(nombre[1:4])  # Muestra las letras desde la posicion 1 hasta la 3


# Inmutabilidad de las variables string
#print("Caracter a cambiar ", nombre[-1])
#nombre[-1] = "a"

#Slicing de strings
#print(nombre[1:4])  # Muestra las letras desde la posicion 1 hasta la 3

#Operaiciones con strings

#upper cambia todas las letras a mayusculas
print(nombre.upper())  # Muestra el string en mayusculas

# lower cambia todas las letras a minusculas
print(nombre.lower())  # Muestra el string en minusculas

#Title cambia la primera letra de cada palabra a mayuscula
print("y cuando desperté, el dinosaurio seguia ahí".title())  # Muestra el string con la primera letra en mayuscula


# strip, lstrip y rstrip eliminan espacios en blanco al inicio y al final del string
nombre = "Diego "
#print(nombre.strip() == "Diego")

# Replace reemplaza un caracter por otro

enunciado = "El carro viejo de mi tio es muy feo"
#print(enunciado)
#print(enunciado.replace("viejo", "nuevo").replace("feo", "bonito"))  # Muestra el string con

# Funciones de comprobacion de strings

variable = '10'

#print(variable.isnumeric())
#print(int(variable)+100)
#print(variable.isalpha()) #isalpha() devuelve True si todos los caracteres de la cadena son letras y hay al menos un carácter, de lo contrario devuelve False.
#print(variable.isalnum()) #isalnum() devuelve True si todos los caracteres de la cadena son alfanuméricos y hay al menos un carácter, de lo contrario devuelve False.
#print(variable.startswith('1')) #startswith() devuelve True si la cadena comienza con el valor especificado, de lo contrario devuelve False.
#print(variable.endswith('p')) #endswith() devuelve True si la cadena termina con el valor especificado, de lo contrario devuelve False.
frase = "El perro de San Roque no tiene rabo"
print(frase.split(" "))