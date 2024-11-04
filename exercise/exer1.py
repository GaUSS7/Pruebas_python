"""
rogramas para la hermanas Ascalin: 
el programa debe leer por cada factura el monto validar que se un numero punto flotante
mayor que cero debe leer quine pago la factura
1.Nives
2.iris
3.Sol
el programa  debe calcuarla el monto total de todas las  facutura monto total pagado 
por cada una de las 3 hermanas


ingresar los datos de cada hermana


 while True:
        try:
            print(
                De las tres hermnas quien hizo gastos ?:
                1.Nives 
                2.Iris
                3.Sol \n)
            seleccion = int(input("Quien hizo mas gastos ?: "))

            match seleccion:
                case 1:
                    nives = monto + 1
                    break
                case 2:
                    iris = monto + 1
                    break
                case 3:
                    sol = monto + 1
                    break
        except ValueError:
            print("Opcion no registrada.")




monto=0
answer="s"


Hermans

sol=0
iris=0
nives=0

Opciones:

seleccion=0

print("\n")

1. valdiacion de la Monto
2. quine pago de las 3 hermanas
3. sumar los contadores de cada uno de las hermanas
4. Mostrar quien tiene el mayor gasto y cuanto le deben las demas


while True:
    try:
        monto = int(input("Ingrese el monto (debe ser mayor que cero.) : "))
        if monto < 0:
            print("monto erroneo, es menor que cero")
        else:
            break
    except ValueError:
        print("se ingreso otra cosa")



while answer in ("S,s"):
    while True:
        try:
            print(
                    De las tres hermnas quien hizo gastos ?:
                    1.Nives 
                    2.Iris
                    3.Sol \n)
            seleccion=int(input("Quien hizo mas gastos ?: "))

            match seleccion:
                case 1:
                    nives = monto + 1
                    total = monto +1
                    break
                case 2:
                    iris = monto + 1
                    total = monto + 1
                    break
                case 3:
                    sol = monto + 1
                    total = monto + 1
                    break
        except ValueError:
            print("Opcion no registrada.")

    try:
        answer=(input("Desea continuar ?:"))
    except ValueError:
        print("Ingreso otra cosa \n")



total=nives+sol+iris
total= total/3

if sol > nives and sol > iris:
    print("factura de las tres Hermanas: \n")
    print(f
        Sol tine un gasto de: {sol}$
        )
elif nives > sol and nives > iris :
    print("factura de las tres Hermanas: \n")
    print(f
        Nieves tine un gasto de: {nives}$
        )
elif iris > nives and iris > sol:
    print("factura de las tres Hermanas: \n")
    print
         Nieves tine un gasto de: {nives}$
        )


       Debemos mostrar cuanto debe cada hermana, las cuotas es lo que determianara si deben o no
       cada una tendra un monto base, (el monto al ir incremnetando se estan endeudando )
       el monto ira incrementando 


       Entonces: lo que quieres saber cuanto debe la hermana que hizo mayores gastos y cuanto le deben las demas 

       volvera hacer el ejercisio ya sabiendo que el codigo busca saber quien pago las facturas y quienes le deben
       mostrar por pantalla el total de la factura el monto de cada hermana y aquien le deben, quien debe y quien no debe
       validar lo validable


        python ./exercise/exer1.py
 """
 
answer="s"
nieves=0
sol=0
iris=0
monto=0
total=0
while answer in ("S" , "s"): #este bucle se encargara de repetir el codigo si se desea otra factura
    
    while True:
        try:
            monto=float(input("Ingrese el monto inicial: "))
            if monto > 0: 
                break
            else:
                print("ERROR. el dato ingresado no puede ser cero o menor de cero")
        except ValueError:
            print("ERROR. Tipo de dato erroneo.")
    print('\n')

    while True: #este ciclo validara cual de las tres hermanas realizo el pago.
        try:
            print("""\t Selecione cual de las tres hermanas realizara el pago: 
          \t 1.) Nieves.
          \t 2.) Sol.
          \t 3.) Iris. """)
            seleccion=int(input("Cual fue ?: "))
            if seleccion in (1,2,3):
                break
            else:
                 print("ERROR. El dato ingresao no esta en la seleccion")
        except ValueError:
            print("ERROR. Tipo de dato erroneo.")
    print('\n')
    
    match seleccion:
        case 1:
            nieves+=monto
        case 2:
            sol+=monto
        case 3:
            iris+=monto
            
    total+=monto #esta varible de aqui se encargara de acumular el total de veces que se halla incrementado el monto.
    print('\n')
    while True:
        try:
            answer=str(input("Desea otra Factura (s,n) ? :"))
            if answer in ("s","S","n","N"):
                break
            else:
                print("ERROR. dato ingresso no se encuentra  en la seleccionada.")
        except ValueError:
            print("ERROR. Tipo de dato erroneo.")


cuota=total/3
c=round(cuota,2)
print(f"""El Monto es de: {monto}$
      \t La cuota es de {c}$
      \t El monto  de Nieves es de: {nieves}$
      \t El monto  de Sol es de: {sol}$
      \t El monto  de Iris es de: {iris}$ """)
print("\n")

if nieves > c:
    print(f"A nieves  le deben: {format(nieves - c)}$")
elif nieves < c:
     print(f"nieves debe: {format(c - nieves)}$")
else:
    print('nieves no debe, ni le deben')
print('\n')

if sol > c:
    print(f"A Sol  le deben: {format(sol - c)}$")
elif sol < c:
     print(f"sol debe: {format(c - sol)}$")
else:
    print('sol no debe, ni le deben')
print('\n')

if iris > c:
    print(f"A Iris  le deben: {format(iris - c)}$")
elif iris < c:
     print(f"Iris debe: {format(c - iris)}$")
else:
    print('Iris no debe, ni le deben')
    



















    




       


            
       

   

    
