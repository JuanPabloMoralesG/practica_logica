"""
Solicita al usuario que ingrese una frase.
Imprime la longitud de la frase.
Convierte la frase a mayúsculas y a minúsculas.
Elimina los espacios en blanco al principio y al final de la frase.
Reemplaza todas las ocurrencias de una palabra específica en la frase (e.g., "Python") 
    por otra palabra (e.g., "programación").
Divide la frase en palabras y las imprime en una lista.
"""
s = input()
print(len(s),s.upper(),s.lower(),s.strip(),s.replace("a","W"),s.split(),sep="\n")