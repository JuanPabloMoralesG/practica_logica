"""
Problema:

Supón que tienes una lista de datos mixtos (cadenas que pueden contener números y letras).
Crea una función que acepte esta lista y haga lo siguiente:
Usa filter() y str.isdigit() para extraer solo las cadenas que contienen solo números.
Usa filter() y str.isalpha() para extraer solo las cadenas que contienen solo letras.
Usa map() para convertir todas las cadenas numéricas extraídas a enteros.
Devuelve una tupla con la lista de números enteros y la lista de letras.
"""
l = ["12","23234", "qwersda", "1212", "12er34"]
print(l)
nums = list(filter(lambda x :x.isdigit(),l))
print(nums)
letras = list(filter(lambda x: x.isalpha(),l))
print(letras)
nums = tuple(map(int,nums))
print(nums)
print([nums,letras])