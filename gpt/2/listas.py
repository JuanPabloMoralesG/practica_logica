"""
Problema:

Crea una función que acepte dos listas de números de igual longitud.
Usa zip() y enumerate() para crear una lista de tuplas donde cada tupla contenga el 
    índice y el par de valores correspondientes de las dos listas.
Usa all() para verificar si todos los pares de valores están en orden creciente.
Usa any() para verificar si existe algún par en el que el valor de la primera lista 
    sea mayor que el valor de la segunda lista.
Ordena la lista de tuplas por el segundo valor en cada tupla.
"""


l1 = [*range(0,10,2)]
l2 = list(range(10,20,2))
print(l1,l2)
l = list(enumerate(zip(l1,l2)))
print(l)
r = any(map(lambda x: x[1][0]>x[1][1],l))
print(r)
r = all(sorted(l,key=lambda x: x[1]))
print(r)

new = list(sorted(l,key=lambda x: x[1][1], reverse=True))
print(new)