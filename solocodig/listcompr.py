
"""
Los elementos de la sucesión S1, está conformado por los elementos de la sucesión S que son múltiples de 3.

Los elementos de la sucesión S2, está conformado por los elementos de la sucesión S1 elevado al cuadrado.

Finalmente, el programa deberá mostrar la suma de los elementos de la sucesión S2, que sean mayores a 2000
"""
s = list(range(10,101,2))

s1 = list(filter(lambda x: x%3 ==0, s))

s2 = list(map(lambda x: pow(x,2), s1))

out = sum(filter(lambda x: x>2000,s2))

print(s,s1,s2,out,sep="\n")