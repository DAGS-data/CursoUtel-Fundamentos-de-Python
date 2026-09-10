


mi_lista = [1,2,3,4,5,6,7,8,9,10]

#print(mi_lista[0])

nombres = ['Diego','Juan','Pedro','Maria','Jose']
print(nombres[1])

#Append agrega al final de la lista
nombres.append('Luis')
print(nombres)

# Insert agrega en la posicion que le indiquemos
nombres.insert(2,'Ana')
print(nombres)


# TUPLAS 

mi_tupla = ("Diego",31,"Mexico")
print(mi_tupla[0])


#mi_tupla[2] = "USA" # Esto no se puede hacer, las tuplas son inmutables

#SET

mi_conjunto={1,1,1,1,1,2,3,4,5,6,7,8,9,10}
print("Mi conjunto: ",mi_conjunto) # Los conjuntos no permiten elementos duplicados

mi_conjunto.add(11) # Agrega un elemento al conjunto
print("Mi conjunto: ",len(mi_conjunto))

#Diccionario 

mi_diccionario = {"Llave":"valor"}
print("Mi diccionario: ",mi_diccionario)
mis_alumnos = {"Diego":10,"Juan":10,"Pedro":7}
print("Calificación de Pedro: ",mis_alumnos["Pedro"])

print(mis_alumnos.keys())
print(mis_alumnos.values())

mis_alumnos["Maria"] = 9
print(mis_alumnos)