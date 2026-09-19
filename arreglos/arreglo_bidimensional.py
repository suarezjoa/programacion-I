# Arreglo bidimensional (matriz)
# Un arreglo de 2 dimensiones organiza los datos en filas y columnas.
# En Python se representa como una lista de listas.

# Matriz de 3 filas x 4 columnas
matriz = [
    [1, 2, 3, 4],     # fila 0
    [5, 6, 7, 8],     # fila 1
    [9, 10, 11, 12],  # fila 2
]

filas = len(matriz)
columnas = len(matriz[0])

print("Filas:", filas, "- Columnas:", columnas)

# Acceso a un elemento: matriz[fila][columna]
print("Elemento en fila 1, columna 2:", matriz[1][2])

# Modificar un elemento
matriz[0][0] = 100
print("Elemento en fila 0, columna 0 despues de modificar:", matriz[0][0])

# Recorrido con dos bucles anidados (mostrar la matriz)
print("\nContenido de la matriz:")
for f in range(filas):
    linea = ""
    for c in range(columnas):
        linea = linea + str(matriz[f][c]).rjust(5)
    print(linea)

# Suma de todos los elementos
suma_total = 0
for f in range(filas):
    for c in range(columnas):
        suma_total = suma_total + matriz[f][c]

print("\nSuma de todos los elementos:", suma_total)

# Suma por fila
print("\nSuma de cada fila:")
for f in range(filas):
    suma_fila = 0
    for c in range(columnas):
        suma_fila = suma_fila + matriz[f][c]
    print("  Fila", f, "->", suma_fila)

# Suma por columna
print("\nSuma de cada columna:")
for c in range(columnas):
    suma_columna = 0
    for f in range(filas):
        suma_columna = suma_columna + matriz[f][c]
    print("  Columna", c, "->", suma_columna)

# Crear una matriz vacia (3x3) y cargarla con la tabla de multiplicar
tabla = []
for f in range(3):
    fila_nueva = []
    for c in range(3):
        fila_nueva.append((f + 1) * (c + 1))
    tabla.append(fila_nueva)

print("\nTabla de multiplicar 3x3:")
for f in range(3):
    linea = ""
    for c in range(3):
        linea = linea + str(tabla[f][c]).rjust(4)
    print(linea)
