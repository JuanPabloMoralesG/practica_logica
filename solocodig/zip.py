"""
Desarrollar un  script en python para mostrar en pantalla el nombre,
 país y puntaje de cada jugador, cuya información se encuentra almacenada 
 en 3 diferentes listas.
"""
players = ['Alvaro Revoredo', 'Mike Frist', 'Paula Jimenez','Gonzalo Chacaltana','Felipe Ayala']
countries = ['Uruguay','Brasil','México','Perú','Chile']
scores = [89.2,81.8,83.4,82.6,80.9]

print(*zip(players,countries,scores))


"""
Desarrollar un programa en python que muestre en pantalla el nombre,
 país de origen y puntaje obtenido de cada jugador, ordenados según 
 su puntaje de mayor a menor y viceversa.
"""
l =list(zip(players,countries,scores))
print(sorted(l,key=lambda x: x[2],reverse=True))
print(sorted(l,key=lambda x: x[2]))