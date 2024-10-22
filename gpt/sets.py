"""
Problema: Escribe un programa que:

Cree dos conjuntos de números enteros.
Imprime la unión de ambos conjuntos.
Imprime la intersección de ambos conjuntos.
Imprime la diferencia entre el primer conjunto y el segundo.
Imprime la diferencia simétrica entre ambos conjuntos.
Agrega un nuevo número a ambos conjuntos y luego elimínalo.
"""
s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9}
print(s1.union(s2), s1.intersection(s2),s1.difference(s2),s2.difference(s1),sep="\n")
s1.add(0)
s2.add(0)
print(s1, s2, sep="\n")
s1.discard(0)
s2.remove(0)
print(s1, s2, sep="\n")
