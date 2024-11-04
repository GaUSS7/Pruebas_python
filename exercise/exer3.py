"""
se utulizara un ciclo for para soliciatar unos datos, los cuales son: 
El sexo de la perosona.
soltero , casado , divorciado , viuda .
ingresar la edad de entre 18 a 60

al finalizar el ciclo se mosrtrara por pantalla.

edad promedio de las mujeres casadas 
mayor edad de las muejeres
que porcentaje de los hombres estan divorcidos
menor edad de los hombres solteros

"""
while True:
    try:
        nperon=int(input("Cuantas personas se registran hoy."))
        if nperon < 1:
            print("ERROR. se ingreso un valor menor a 1.")
            print("\n")
        else:
            break
    except ValueError:
        print("ERROR. Dato erroneo")

print("\n")

#Datos solicitados por pantalla
inf_sexo=0
inf_estado=0
inf_edad=0

#Datos al finalizar el ciclo
promedio=0
edad_mayorM=0
edad_menorH=0
hombres_divorciados=0


#datos extras
edadacuont=0
edadcont=0
hombrescontador=0
divorcio=0


for n in range (1, nperon+1):
    #Datos de acceso.
    hombre=0
    mujer=0

    while True:
        try:
            inf_sexo=int(input("Ingrese su sexo. 1.)Hombre 2.)Mujer \n \n"))
            if inf_sexo in (1,2):
                break
            else:
                print("ERROR. Opcion erronea.")
        except ValueError:
            print("ERROR. Dato erroneo")

    print("\n")

    while True:
        try:
            inf_estado=int(input("Ingrese su estado sivil: \n1.Soltero/a \n2.Casado/a \n3.Divorciado/a \n4.Viudo/a  \n \n)"))
            if inf_estado in (1,2,3,4):
                break
            else:
                print("ERROR. Opcion erronea")
        except ValueError:
            print("ERROR. dato erroneo.")

    print("\n")

    while True:
        try:
            inf_edad=int(input("Ingrese  la edad entre 18 a 60 \n \n"))
            if inf_edad >=18 and inf_edad <=60:
                break
            else:
                print("ERROR. opcio mal ingresada.")
        except ValueError:
            print("ERROR. Dato erroneo")


    match inf_sexo:
        case 1:
            hombre=1
            hombrescontador+=1
        case 2:
            mujer=2
            if inf_edad >=30:
                edad_mayorM+=1
                


    match inf_estado:
     case 1:
        if inf_sexo == 1 and inf_edad <= 29:
            edad_menorH += 1
     case 2:
        if inf_sexo == 2:
            edadacuont += inf_edad
            edadcont += 1
     case 3:
        if inf_sexo == 1:
            divorcio += 1



                

print("\n")





print("\n")

# Cálculo del porcentaje de hombres divorciados
if nperon > 0:
    porcentaje_hombres_divorciados = (divorcio / nperon) * 100
    print(f"El porcentaje de hombres divorciados es de: {porcentaje_hombres_divorciados:.2f}%")
else:
    print("No se han registrado personas.")

# Cálculo del promedio de edad de mujeres casadas
if edadcont > 0:
    promedio_edad_mujeres_casadas = edadacuont / edadcont
    print(f"El promedio de edad de las mujeres casadas es de: {promedio_edad_mujeres_casadas:.2f}")
else:
    print("No hay mujeres casadas registradas.")

# ... (resto de los prints)









try: 
    print(f"El promedio de las mujeres casadas es de: {edadacuont/edadcont}")
except ZeroDivisionError:
    print("No se peude realizar la division para el promedio de las muejeres casadas, division entre zero.")

print(f"La cantidad de muejeres de mayor edad es de: {edad_mayorM}")   

c=divorcio/nperon*100
d=round(c,2)
try:
    print(f"El el porcentaje de los hombres Divorciados es de: {d}")
except ZeroDivisionError:
    print("ERROR. No se pudo sacar la el promedio de la hombres Divorciados. Divsision sobre cero.")

print(f"La cantidad de hombres de menor edad solteros  es de: {edad_menorH}") 

            

   