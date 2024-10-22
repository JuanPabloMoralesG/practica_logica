cadena = "Python Programming is Fun!"
cadena_inv = "".join(reversed(cadena))
print(cadena_inv)

nombres = ["Ana", "Luis", "María", "Juan", "Pedro"]
calificaciones = [85, 92, 88, 79, 95]
d = dict(zip(nombres,calificaciones))
print(d)

numeros = [4, 5, 6, 7, 5, 6, 4, 6, 5, 4, 4]

set_numeros = set(numeros)
l = list(filter(lambda x: x[1],set(map(lambda x: (x,numeros.count(x)),numeros))))
print(l)


# suma y producto
numero = 12345
n = str(numero)
print(sum(int(i)  for i in n))

# cambio de base

dec = 255
print(hex(dec)[2:],dec,oct(dec)[2:],bin(dec)[2:])