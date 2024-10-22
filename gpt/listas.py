"""
Problema: Escribe un programa que:
Cree una lista de números enteros.
Imprima la cantidad de elementos en la lista.
Imprima el número máximo y el número mínimo de la lista.
Imprima la suma de todos los números de la lista.
Imprime una versión ordenada de la lista en orden ascendente.
Utiliza enumerate() para imprimir los índices y los valores de la lista.
"""
l = [2,34,53,3,723,3123,723,23,64]
print(len(l), max(l),min(l),sum(l),sorted(l),*enumerate(l),sep="\n")