"""
Problema:

Crea una función que acepte una lista de cadenas de texto.
Usa filter() y una función lambda para filtrar solo las cadenas que son palíndromos. 
    Considera solo los caracteres alfanuméricos y ignora los espacios y signos de puntuación.
Usa map() para normalizar cada cadena, eliminando espacios y convirtiendo a minúsculas.
Devuelve una lista con las cadenas que son palíndromos y que cumplen con las condiciones anteriores.
"""

l = ["12321","Holoh", "Hola", "algo","Palindromo", "1joj1"]

l = list(map(lambda x: (x.lower().strip()),l))
p = list(filter(lambda x: x.isalnum() and x == "".join(reversed(x)),l))
print(p)