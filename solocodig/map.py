"""
Desarrollar un programa en python que muestre en pantalla el récord
 académico de las notas de un alumno: Nombre del curso,  
 Notas obtenidas (Nota 1 y Nota 2), Nota Final y Estado ("Aprobado" o "Desaprobado"). 
 Para aprobar el curso, la "Nota Final" debe ser mayor o igual a 13. Además calcular 
 y mostrar el "Promedio Final Anual" y estado final de aprobación de todos los cursos 
 del año en curso.
"""
Cursos = ['Programación de Sistemas','Estadística Básica', 'Algebra Lineal', 'Matrices Distribuidas', 'Redes Neuronales']
n1 = [15,18,12,19,13]
n2 = [18,16,13,16,18]

l = list(zip(Cursos,n1,n2))

nf = [(x+y)/2 for x,y in zip(n1,n2)]
promedio_final = sum(nf)/len(nf)

for x in range(len(Cursos)):
    print(f"Nombre:{Cursos[x]}\n Nota1:{n1[x]}\n Nota2:{n2[x]}\n Nota Final:{nf[x]}\n Estado:{"Aprobado" if nf[x]>13 else "reprobados"}")