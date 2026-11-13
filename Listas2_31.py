#Dada una lista de números enteros y un entero k, escribir una función que:
#Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
#Devuelva una lista con aquellos que son múltiplos de k.

'''
def crearLista(k,lista):
    menores=[]
    mayores=[]
    iguales=[]
    multiplo=[]

    for i in lista:
        if i<k:
            menores.append(i)
        elif i>k:
            mayores.append(i)
        else:
            iguales.append(k)

        if i%k==0:
            multiplo.append(i)

    return menores,mayores,iguales,multiplo

#programa Principal

numeros=[4,9,8,7,2,0,1,7,9,54,5,42,9,3,1,7,5,12,45,9,98,99,66,30,31,35,71,63]
k=int(input("Ingrese un numero-> "))
lista1,lista2,lista3,lista4=crearLista(k,numeros)

print(f"Lista de Menores de {k}: {lista1} ")
print(f"Lista de Mayores de {k}: {lista2} ")
print(f"Lista de Iguales a {k}: {lista3} ")
print(f"Lista de Multiplos de {k}: {lista4} ")'''



#Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. 
# Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

'''
num=int(input("Digite un numero-> "))
tabla=[]

for i in range(1,11):
    mul=num*i
    tabla.append(mul)

print(tabla)'''





#Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida.
#Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].
'''
def inv_lista(lista):
    listainversa=[]
    longitud=len(lista)-1

    for i in range(longitud,-1,-1):
        listainversa.append(lista[i])

    return listainversa

# def inversa(palabra):
#     reversa = ''
#     for i in palabra: 
#         reversa = i + reversa
#     return reversa

lista=["Pedro","Juan","Pepe","Luisa"]
print(lista)
lista.reverse()
print(lista)
print(inv_lista(lista))'''


#Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. 
# Por último, muestra los números ordenados de menor a mayor.
'''
numeros=[]
num=int(input("Ingrese un numero -> "))

while num!=0:
    numeros.append(num) 
    num=int(input("Ingrese un numero -> "))

print(numeros)
#numeros.sort() #Ordenar ascendentemente
print(numeros)
max=0
longitud=len(numeros)

for i in range(longitud):
    for j in range(longitud):
        if numeros[i]<numeros[j]:
            max=numeros[i]
            numeros[i]=numeros[j]
            numeros[j]=max

print(numeros)'''

#Tuplas - inmutables
'''
t=("Juan",32,"31238471","Bogota")
print(t[1])
#t[1]=50

a="Maria"
b="Medellin"
c=35
d="312154545"

t1=a,b,c,d #empaquetado
print(t1)
print(a)

w,x,y,z=t #desempaquetado

print(w)
print(x)
print(y)
print(z)

for i in t1:
    print(i)'''





#Diccionarios

alimentos= {}
alimentos["frutas"]=["Fresa","Naranja","Piña"]
alimentos["vegetales"]=["Lechuga","Espinaca"]
alimentos["Lacteos"]=["Yogurt","queso"]

print(alimentos)
alimentos["frutas"][1]="Manzana"
print(alimentos["frutas"][1])
for i in alimentos["frutas"]:
    print(i)


for key,valores in alimentos.items():
    print("Clave ->",key)
    longi=len(valores)
    valores.append("agregar")
    for i in range(longi):
        valores[i]="cambio"

print(alimentos)
        
