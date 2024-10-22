"""
Problema: Escribe un programa que:

Cree dos listas de números.
Usa zip() para combinar ambas listas en una lista de pares.
Usa map() para sumar los pares correspondientes de las dos listas.
"""

l1= [1,2,3,4]
l2= [4,3,2,1]
print(*map(lambda x : x[0]+x[1],zip(l1,l2)))