"""
Problema: Escribe un programa que:
Cree una lista de números enteros.
Usa map() y una función lambda para elevar al cuadrado cada número de la lista.
Usa filter() y una función lambda para obtener solo los números pares de la lista.
Usa reduce() (importado desde el módulo functools) y una función lambda para calcular 
    el producto de todos los números en la lista.
"""
from functools import reduce
l = [1,2,3,23,10,20,25,32]
print(l)
l = list(map(lambda x: pow(x,2), l))
print(l)
l = list(filter(lambda x: x%2==0,l))
print(l)
l = reduce(lambda x,y: x*y ,l)
print(l)