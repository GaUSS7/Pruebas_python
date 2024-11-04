#practicas de listas y funciones.
""" Crear llistas y llamarlas """
"""list1 =[] #lista  vacia
list2= [1,2,3,4,5] # lista con datos dentro

""""""
inser=int(input("Ingresa algo a la lista vacia: "))#si la lista es de numeros, se debe respetetar eso.
list1.append(inser)
print(list1)

print('\n')

inser2=int(input("Ingresa algo a la lista con datos: "))
list2.append(inser2)
print(list2)"""

"""Ambas pueden recibir datos"""

"""tupla=(1,2,3) #tupla con datos dentro
print(tupla[0])
tupla[1]=2
La tupla no se puede alterar 
"""

"""La iteracion me debe tomar todos los datos para que me suelte """
def name():
    while True:
        nombre=(input("Ingrese su nombre: "))
        partes=nombre.split(" ")
        if all(parte.isalpha() for parte in partes):#investigar el all, haca que si todo da true entra y si no, sale
            return nombre
        else:
            print("Por favor, ingrese solo letras en su nombre.")
        

def cedulaa():
    while True:
        cedula=(input("Ingrese su cedula: "))
        if cedula.isdigit() and (len(cedula)<=8 and len(cedula)>=7):# aqui estoy pidiendo que la cedula se digit y que este dentro del intervalo de datos que estoy solicitando
            return cedula
        else:
              print("ERROR, la cédula debe tener entre 7 y 8 dígitos numéricos.")




def cedulaforing():
    while True:
        cdedulaf=input("Ingrese su cedula: ")
        if len(cdedulaf)<=8 and len(cdedulaf)>=7:
            if "j" in cdedulaf : #los datos de busqueda tipo string, van del lado izquierdo
                return cdedulaf
            else:
                return f"Su ceula no es extrajenra: {cdedulaf}"
        else:
              print("ERROR, la cédula debe tener entre 7 y 8 dígitos numéricos.")



#el dicionario busacara la key, no los datos que lleve adentro
def busqueda():
    dect = {"Nombre": "Gabriel" , "Edad": 30,  "Apellido": "Torres"}
    while True:
        serch=input("Ingrese lo que quiere buscar: ")
        for a in dect:
            if serch in a:
                return (f"{serch} es {dect[a]} ")
            else:
                print("No hay nada de eso.")
                break



"""La poscion del input marca problema con el for, de ahi que por alguna razon el error me lo diera el while, si dejaba el for, seguia normal"""
"""la funcion in sirve para muchas cosas"""
def busqueda2():
    dect = {"Nombre": "Gabriel" , "Edad": 30,  "Apellido": "Torres"}
    while True:
        serch=input("Busqueda: ")
        if serch in dect:
            return f"EL {serch} es {dect[serch]}"
        else:
            print("no hay nada de eso.")



"""una funcion para ceula extranjeras, datos dentro de funciones"""
    
recivename=name()
print(f"Su nombre es: {recivename}")

print("\n")

recivecedula=cedulaa()
print(f"Su cedula es: {recivecedula}")

#cedula extranjera
cedulafe=cedulaforing()
print(cedulafe)
