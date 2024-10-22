"""
Crea una función que acepte una lista de cadenas de texto, donde 
    cada cadena representa una fecha en formato DD/MM/YYYY.
Usa map() y una función lambda para convertir cada fecha en formato YYYY-MM-DD.
Usa filter() para eliminar las fechas que son anteriores a un año específico (por ejemplo, 2000).
Usa reduce() para contar cuántas fechas quedan después de filtrar.
"""


l = ["12/23/2023","4/5/2345","76/54/6787","67/23/1232"]
print(l)
l = list(map(lambda x: x.split("/")[2]+"-"+x.split("/")[1]+"-"+x.split("/")[0],l))
print(l)
l = list(filter(lambda x: int(x.split("-")[0])> 2000 and int(x.split("-")[0])< 3000,l))
print(l)