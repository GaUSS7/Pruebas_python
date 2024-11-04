""" Practicas de tuplas,listas,funcioens
escribir una funcion que lee uba cedula con la funcin .isadigit()"""


"""Tengo un probema, no me retorna los datos, no se porque, aun
pareceser que el problema se debia algun mal entidimiento de tipo de datos
los lin no se llevan con los int, pero si con los strings"""

"""def cedulaINF(cedula,valid):
       if valid == True:
             if len(cedula) <=8 or len(cedula) <=7:
                    return f"Su cedula es: {cedula}"
             else:
                 return "ERROR"
       

cedula=input("Ingrese su cedula: ")
while not(cedula.isdigit()==True):
    cedula=input("Ingrese su cedula: ")
    if cedula.isdigit()==True:
        break

#confirmar que es str de tipo numerico
confirmarCedula=cedulaINF(cedula,cedula.isdigit())
print(confirmarCedula)

"""

#Listas y tuplas: 

lista=[1,2,4,5,6,6]
print(lista)

print(lista[4])
print(lista[-1])
lista[5]=7
print(lista[-1])
print(lista)
print(lista.pop())
print(lista)


print(lista[1:4])
print(lista[0:-1])

tuple[1,3,4]
print(tuple)