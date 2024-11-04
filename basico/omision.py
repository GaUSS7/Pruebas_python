'''
Pruebas de funciones con valores por omision
'''

"""def reintenetar(prompt,intentos=None,messege=''):
    for n in range (1,intentos+1):
        ok=input(prompt)
        if ok in ('s','si'):
            return "Saliste"
        else:
            intentos-=1
            print(messege,f"Te quedan {intentos} intentnos mas")
        if intentos == 0:
            return "Te quedaste sim intentos "


probar=reintenetar("Quieres salir: ",5,"Intentantalo")
print(probar)
"""

tupla= [1,2,3,4]
validar=int(input("ingrese un dato a la tupla: "))
print("ahora tiene: ",len(tupla))


while not(validar in tupla):
    validar=int(input("ingrese un dato a la tupla: "))
    if validar in tupla:
        break
    else:
        print("Vuelvalo a intentar.")


######################################################

numeros = array=['i']
print(len(numeros))
print(numeros)

numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)

print(len(numeros))
print(numeros)






"""for n in tupla:
    n=input("Ingrese un numero entre la tupla")
    if n in tupla[1,2,3,4]:
        break
    elif not(n in tupla[1,2,3,4]):
        print("intentalo otra vez")
    """





def validEntrada(dato,dato2="ERROR FATAL"):
    while True:
        lista=[1,2,3,4,]
        validar=int(dato)
        if validar in lista:
            return validar
        elif not(validar in lista):
            print(dato2)
            dato=int(input("Vuelvelo a intentar."))

def validarNUM(dato):
    while True:
        try:
            validar=int(input(dato))
            if validar > 0:
                return validar
        except ValueError:
            print("error")
    

validar=int(validarNUM(":"))
dato=validEntrada(validar)
match dato:
    case 1:
        print("Opcion 1")
    case 2:
        print("Opcion 2")
    case 3:
        print("Opcion 3")
    case 4:
        print("Opcion 4")
