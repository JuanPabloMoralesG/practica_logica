"""
Desarrollar un script en python que almacene en una lista, 
las contraseñas que cumplan con las reglas de validación.

Reglas de validación de contraseña:
1. Debe tener más de 8 caracteres.
2. Debe tener al menos uno de los siguientes símbolos "@&$_".
3. Debe tener al menos un número.
4. Debe tener al menos una vocal en minúscula.
"""
passwords = ['123456','sistemas','xf@9ops_','segura','zx3kulP@i_','secreto','v8$nbep1bf_','cumple1304']

def validate(password:str):
    pas_len = len(password)>8
    symbols = not set('@&$_').isdisjoint(password.lower())
    numbers = not set('1234567890').isdisjoint(password.lower())
    vowels = not set('aeiou').isdisjoint(password.lower())
    return all([pas_len,symbols,numbers,vowels])


l =  list(filter(validate,passwords))
print(l)
