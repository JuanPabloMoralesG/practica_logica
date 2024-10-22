"""
Problema:

Supón que tienes una lista de diccionarios donde cada diccionario representa una 
    fila de datos de una tabla con las claves 'Nombre', 'Edad' y 'Salario'.
Crea una función que acepte esta lista de diccionarios.
Usa map() y lambda para extraer los salarios y calcular el salario promedio.
Usa filter() para obtener solo aquellos registros con salarios superiores al promedio.
Usa sorted() para ordenar los registros filtrados por edad, de menor a mayor.
"""

d = [{"nombre":"nom","edad":50,"salario":20000},
     {"nombre":"nom2","edad":23,"salario":30000},
     {"nombre":"nom3","edad":34,"salario":10000},
     ]

prom = sum(map(lambda x : x["salario"],d))/len(d)
print(prom)

sup = list(filter(lambda x: x["salario"]>prom,d))
print(sup)

edad = list(sorted(d,key=lambda x: x["edad"]))
print(edad)