print("Hello world, bienvenido al curso de Fundamentos de Python")
print("Este es mi primer script de python")

altura = int(input("Ingresa la altura de la pirámide: "))

for i in range(1, altura + 1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)