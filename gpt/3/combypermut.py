"""
Problema:

Crea una función que acepte dos listas de números de igual longitud.
Usa zip() para combinar las listas en una lista de tuplas.
Usa enumerate() para crear una lista de índices y pares de valores combinados.
Usa map() y una función lambda para calcular la diferencia entre los pares de valores.
Usa all() para verificar si todas las diferencias son mayores que un umbral dado.
Usa any() para verificar si alguna diferencia es igual a un valor específico.
"""

l1 = [12,23,21]
l2 = [23,34,43]

lt = list(zip(l1,l2))
print(lt)
le = list(enumerate(lt))
print(le)

dif = list(map(lambda x: x[1][0]-x[1][1],le))
print(dif)

print(all(map(lambda x: x<0,dif)))
print(any(map(lambda x: x == 0,dif)))