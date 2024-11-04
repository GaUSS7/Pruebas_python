def insertvalue():
    global name
    name=0
    print(name)




name="gabriel"
print(name)
insertvalue()
print(name)

dato="+21321312321"
print(len(str(dato)))#los datos numericos no tinen len
for  a in str(dato):
    print(a)

print(not(dato.isdigit()))
"""La poscion infunde en las variblaes gloabale
la funcion al pasar me reconce que hay una variable con el mismo nombre, la esta tomando como lo que es, una variable global
La poscion de las funciones si tine que ver
La variavles detro de las fiuncioens son locales, las diferencias estna en que si el nombre de la varible que tengas en la funcion 
tenga el mismo nombre de una funncion, en ese caso si puede ser globales, pero la mayor parte del tiempo  le asignas ottos valores 
y termina siendo diferente, a la varible global, entonces para usar la varible (el nomnbre) tiene referenciarlo con el global, 
global buscara la variable con ese nombre, y la asignarar como global otra vez (tener en cuenta que antes en la funcion era local)"""
n=0
estudiantes = ["José", "María", "Carlos"]
notas = [
        [15, 16, 17],
        [19, 17, 20],
        [15, 12, 16]
        ]
print ('Estudiante'.ljust(15), 'Nota 1'.center(8), 'Nota 2'.center(8), 'Nota 3'.center(8), 'Promedio'.center(8))
for e, n in zip (estudiantes, notas):
    print(n)
    prom = (n[0] + n[1] + n[2])/3
    print(prom)
    #print (e.ljust(15), str(n[0]).center(8), str(n[1]).center(8), str(n[2]).center(8),str(round(prom,2)).center(8))
    