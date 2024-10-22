"""
Problema: Escribe un programa que:
Cree un diccionario con al menos 5 pares clave-valor.
Imprima la cantidad de pares clave-valor en el diccionario.
Imprima todas las claves y todos los valores del diccionario.
Utiliza get() para recuperar el valor de una clave específica.
Agrega un nuevo par clave-valor al diccionario.
Imprime el diccionario actualizado.
"""
d = {1:"a", 2:"b",3:"c",4:"d",5:"e"}
print(len(d),d.keys(),d.values(),d.items(),d.get(4),sep="\n")
d.update({6:"f"})
print(d)
