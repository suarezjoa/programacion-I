# Arreglo unidimensional (vector)
# Un arreglo unidimensional guarda varios valores del mismo tipo
# en una sola fila. En Python se representa con una lista.

# Creacion del arreglo con valores iniciales
notas = [7, 10, 4, 8, 6]

# Acceso por indice: el primer elemento es el indice 0
print("Arreglo completo:", notas)
print("Primer elemento (indice 0):", notas[0])
print("Ultimo elemento (indice -1):", notas[-1])
print("Cantidad de elementos:", len(notas))

# Modificar un elemento
notas[2] = 9
print("Despues de cambiar el indice 2:", notas)


# Operaciones comunes: suma, promedio, maximo y minimo
suma = 0
for valor in notas:
    suma = suma + valor

promedio = suma / len(notas)

print("\nSuma:", suma)
print("Promedio:", promedio)
print("Maximo:", max(notas))
print("Minimo:", min(notas))

# Busqueda de un valor dentro del arreglo
buscado = 8
encontrado = False
for i in range(len(notas)):
    if notas[i] == buscado:
        print("\nEl valor", buscado, "esta en la posicion", i)
        encontrado = True
        break

if not encontrado:
    print("\nEl valor", buscado, "no se encuentra en el arreglo")

# Crear un arreglo vacio y cargarlo

