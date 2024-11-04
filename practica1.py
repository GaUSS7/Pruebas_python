print("Validcacion (Metodo de la profesora.)")
print("\n")
"""
validacion con un while y con el uso del try exept
"""
while True:
    try:
        a=int(input("Ingrese un nuemero del 1 hasta el 10: "))
        if a>=1 and a<=10:
            break
        else:
            print('\n')
            print("Error. el dato numerico debe  estar entre 1 a 10.")    
    except ValueError:
        print("Error. Se debe ingresar datos numericos. NO de caracter")
        print("")
        

    
              
            
for c in range(1 , 11):
    print(f"{a} x {c} es igual a: {a*c}")


"""
Tines varios metodos de validacio con el ciclo while
tamnbien con los operadores de True o False (not) el cual debes practica
"""