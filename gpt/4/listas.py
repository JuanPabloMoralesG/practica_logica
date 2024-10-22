
# Fitro pro precio y orden alfabetico
productos = [("Manzana", 50), ("Banana", 30), ("Naranja", 50), ("Mango", 20), ("Papaya", 20)]

l = list(sorted(productos,key=lambda x: x[1],reverse=True))
print(l)


# nueva lista con los numeros de ambas listas sin repetir
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

s1 = set(lista1)
s2 = set(lista2)
s3 = s1.union(s2)
print(s3)

