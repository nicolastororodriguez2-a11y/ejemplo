'''Un alumno desea saber cuál será su calificación final en la materia de Lógica Computacional. 
Dicha calificación se compone:
45% del promedio de sus tres calificaciones parciales.
35% de la calificación del examen final.
20% de la calificación de un trabajo final.'''

n1=float(input("Digite la nota uno\n"))
n2=float(input("Digite la nota dos\n"))
n3=float(input("Digite la nota tres\n"))

promedio=(n1+n2+n3)/3
p45=promedio*0.45

notaExamen=float(input("Digite la nota del examen final\n"))
p35= notaExamen*0.35

notaTrabajof=float(input("Digite la nota del trabajo final\n"))
p20=notaTrabajof*0.2

notaFinal=p45 + p35 +p20

print("Su nota final es: ",notaFinal)

if notaFinal>=3:
    print("Usted Aprobo la Materia")
else:
    print("Usted No Aprobo la Materia")

print("Otras intrucciones")

from random import randint
num=randint(1,1)
print(num)





