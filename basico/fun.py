def suma (dato1 , dato2): 
    x = dato1 + dato2
    return print(f"El reuslto es:  {x}")

num1=int(input("Ingrese un dato: "))
num2=int(input("Ingrese un dato: "))
result=suma(num1,num2)
''' 
 Las fucnines pueden recivir datos o no.
 python ./basico/fun.py
'''

'''///////////////////////////////////////'''
print('\n')

''' EL operador NOT se va asegurar que no se cumpla lo que yo no quiero'''
def validacion(dato):
    if dato <= 0:
        print("ERROR, se ingreso un dato menor a cero o cero.")
        return 0
    else:
        return 1

def numNOletra(dato):
    while dato is str(dato):
        dato=int(input("Vuelva a ingresar un dato:"))
        if dato.isdigit() == False:
            break



num3=int(input("Ingrese un dato mayor a uno: "))
validDato=numNOletra(num3)


while not(num3>0): 
     num3=int(input("Ingrese un dato mayor a uno: "))
     valid=validacion(num3)
        
         

        
''' Pruebas de valdidacion'''



    

   