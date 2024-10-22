"""
Problema:

Crea una función que acepte una lista de números enteros y devuelva una 
    lista de números únicos ordenados por su frecuencia de aparición, de mayor a menor.
Usa set() para obtener los números únicos.
Usa map() para contar la frecuencia de cada número usando list.count().
Usa sorted() para ordenar los números por frecuencia en orden descendente.
"""
l = [2,2,3,3,4,4]
s = set(l)
print(s)

c = list(map(lambda x: (x,l.count(x)),l))
s = set(c)
print(s)
c = list(sorted(c,reverse=True))
print(c)