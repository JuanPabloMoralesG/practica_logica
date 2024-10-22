lista_de_listas = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

nueva_lista = [elemento for sub_lista in lista_de_listas for elemento in sub_lista]
print(nueva_lista)

cadenas = ["radar", "python", "level", "world", "madam"]
pal = list(filter(lambda x: x == "".join(reversed(x)), cadenas))
print(pal)

lista_a = [1, 2, 3]
lista_b = [4, 5]
p_cartesiano = [(i, j) for i in lista_a for j in lista_b]
print(p_cartesiano)

enteros = [4, 2, 9, 1, 5, 2, 4, 1, 9]
list_ordenada = [*sorted(list(set(enteros)))]
print(list_ordenada)


nums = [1, 2, 3, 4]
lista_ac = [sum(nums[:i+1]) for i in range(len(nums))]
print(lista_ac)

diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 3, 'c': 4, 'd': 5}
print()

palabras = ["apple", "banana", "cherry", "date", "fig", "grape"]
n = 5
palabras_n = list(filter(lambda x: len(x) == n, palabras))
print(palabras_n)

personas = {'Alice': 30, 'Bob': 25, 'Charlie': 30, 'David': 25}
dic = {}
print(dic)

texto = "Hello world, hello Python. Python is great!"
palabras = texto.lower().split()
set_palabras = set(palabras)
print(set_palabras)







