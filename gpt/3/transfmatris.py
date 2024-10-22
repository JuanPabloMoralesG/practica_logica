"""
Problema:

Crea una función que acepte una lista de listas (una matriz) y devuelva su transposición.
Usa zip() para crear la matriz transpuesta.
Usa map() y list() para convertir las filas originales en columnas en la matriz transpuesta.
Verifica si todas las filas de la matriz original tienen el mismo número de columnas utilizando all() y len().
Verifica si alguna fila en la matriz transpuesta es idéntica a otra fila utilizando any()
"""

m = [[1,2,5],[3,4,6],[7,8,9]]
mt = []
for i in range(len(m)):
    f = list(map(lambda x,i=i: x[i],m))
    mt.append(f)
print(*m, sep='\n')
print('\n',*mt, sep='\n')

print(any(filter(lambda x: x in mt,m)))