'''lis=["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
print(lis[0])

n=0
print(list[n+1])

notas=[]
for i in range(1,7):
    insert=int(input("Ingrese la nota:"))
    notas.append(insert)

print(notas)

#recuerda que a tiene los datos de la lista, y solo los mostrar por iteracion 
for a in lis:
    print(f"Su asignatura es: {a}")'''


"""#Mostrar notas y asiganaturas.
asiganaturas=['Deporte','Quimica','Fisica','Matematica','Recreo']
notas=[]
for a in asiganaturas:
    ingresar=int(input(f"Ingrese su notas de la asignatura {a}: "))
    notas.append(ingresar)

print(notas)#mostrar que si llego los datos a la lista 
print(asiganaturas)#mostrar que si llego los datos a la lista 
n=0
#el delcalr las variables con un cero funciona para recorrera los array, todos los array y listas , slcies se recorren mediante iteracoion
# aqui se le esta asignado los datos que tiene la lista  a una varible creada desde el for para recorrer la lista
for a in asiganaturas:
    print(f"La nota de la asiganatura de {a} es de: {notas[n]}")
    n+=1"""

"""def leernote(strasig):
    asiganturas=[]
    for a in strasig:#aqui se va mandando por iteracion a la lista
        asiganturas.append(a)

    return asiganturas

#nota ten en cuenta que todos los recorridos y asignacion es gracias a los for, tiene que estar pendiente de los datos que quieres mandar a una lista


print("Ingrese las notas las asignaturas que esta cursando: ")

#el split solo le del tipo string
datos=(input("Ingrese su asiganturas: "))
#el split me ayuda picarlos en partes para, luego mandarlos a la funcion, que recive los datos, en la lista
asignaturas=leernote(datos.split('/'))#el parametro de la funcion pasa todo de golpe
print(asignaturas)

notas=str(input("Ingrese sus notas de las asignturas: "))
notasver=leernote(notas.split('/'))
print(notasver)

n=0
for a in asignaturas:
    print(f"La asignatura {a} tiene la nota: {notasver[n]}")
    n+=1"""

# list1=[1,3,4,5,6]
# #con este no hace falta iterar 
# print(3 in list1)
# print(8 in list1)

# protabs="Hola pendejo"
# print( "a"  in protabs)


    

"""prueba de variables globales."""

#def noteandpromedi(nota,promedio):
    
"""lis1=[]

notas=input("Ingrese sus notas: ")
guardar=notas.split(" ")
for a in guardar:
   save=int(a)
   lis1.append(save)

print(guardar)
print(lis1)"""



#
print(20-10)


global saldo
saldo=200

def retirar(cantidad):
   global saldo
   saldo -= cantidad
   return saldo
 


valor=retirar(12)
print("")
print(valor)

print(600/0.30)

listq=[1,2,3,4,5,6]
n=0
for a in listq:
   print(f"posci")
   n+1

"""Despues de pasar por la funcion"""
"""La lista no lograria ser cambiada porque se estba 
creando otra lista, de ahi que no hubiera 
cambios, lo que tenia que hacer es cambiar el parametro de recivia la funcion"""