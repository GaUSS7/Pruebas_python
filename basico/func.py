def validar(valor):
    while True:
        try:
            numero = int(input(valor))
            if numero > 1:
                return f"El número ingresado es {numero}"
            else:
                print("Ingrese un número entero mayor que 1.")
        except ValueError:
            print("Debe ingresar un número entero.")

resultado = validar("Ingrese un valor mayor a 1: ")
print(resultado)
'''
Podemos hacer que los datos registren de una el dato que se envio a la funcion
'''

print('\n')
def validar(dato):
    while True:
        try:
            numero=int(input(dato))
            if numero > 0:
                return numero
        except ValueError:
            print("DATO ERRONEO")
    
    




def calculadora(dato,dato2):
    restl = dato + dato2
    return restl


print("Ingrese los numeros los cuales usted quiera sumar: ")
num1=validar("Valor 1: ")
num2=validar("valor 2: ")
resultado=calculadora(num1,num2)
print(f"El resultado es: {resultado}")



"""
////////////////////////////////////////////////////////////////////////////////////
"""

"""
te pide saber cunato son las cantidades de hombres y muejers que ingreasaron y el porcentaje de los hombres
"""
hombre=0
mujer=0
total=0
def validar(dato):
    while True:
        try:
            numero=int(input(dato))
            if numero in(1,2):
                return numero
        except ValueError:
            print("Dato erroneo")



while True:
    print("Contador de hombres y mujeres")
    print('\n')

    personas=validar("Usted es hombre o mujer : 1)si 2)no ")
    match personas:
        case 1:
            hombre+=1
        case 2:
            mujer+=2
    total+=1
    pregunta=validar("Deseas salir del contador: 1)si 2)no")
    if pregunta == 1:
        break


print(f"EL total de peronas fue de: {total}")
print(f"EL total de mujeres fue de: {mujer}")
print(f"EL total de hombres fue de: {hombre}")

porcentaje=(hombre*100)/total
c=round(porcentaje,2)
print(f"EL porcentaje de los hombres fue de: {c}")
