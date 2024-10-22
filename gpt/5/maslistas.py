numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares = list(map(lambda x: pow(x, 2), filter(lambda x: x % 2 != 0, numeros)))
print(impares)

palabras = ["apple", "banana", "cherry", "date", "fig", "grape"]

long_palabras = list(map(len, palabras))
print(long_palabras)

nums = [3, 5, 6, 9, 10, 12, 15, 20]

mult_3 = list(map(lambda x: x * 2, filter(lambda x: x % 3 == 0, nums)))
print(mult_3)

#(0 °C × 9/5) + 32

celsius = [0, 20, 37, 100]

far = [(i*9/5)+32 for i in celsius]
print(far)

palabras = ["apple", "banana", "cherry", "date", "fig", "grape"]
n = 4

log_palabras = [len(i) for i in palabras if len(i) > n]
print(log_palabras)

num1 = [1, 2, 3, 4, 5]

tup_nums = [(i, pow(i, 3)) for i in num1]
print(tup_nums)

cadenas = ["apple", "banana", "cherry", "date", "fig", "grape"]

letra_a = list(map(lambda x: x.upper(), filter(lambda x: x.find("a") != -1, cadenas)))
print(letra_a)


lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

l3 = list(zip(lista1, lista2))
print(l3)

num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([pow(i, 2) for i in num3 if i % 2 == 0])
