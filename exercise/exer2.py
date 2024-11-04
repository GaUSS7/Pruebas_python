'''
sexo=0
edocivil=0
edad=0
hombre=0
mujer=0
Solterocont=0
casdocont=0
divorcidocont=0
viudacont=0
edadmenor=0
edadmayor=0
n=0


""" 
se ingresa la cantidad de veces que deseaa repetir.
"""
while True:
    try:
        n = int(input("Cuantos datos desea ingresar:"))
        break
    except ValueError:
        print("ERROR. DATO")

for n in range(n):
    while True:
        try:
            print("\n")
            sexo=int(input("1.hombre 2.mujer :"))
            if sexo in (1,2):
                break
            else:
                print("\n")
                print("ERROR")
        except ValueError:
            print("DATO ERRONEO.")

    match sexo:
        case 1:
            hombre = +1

        case 2:
            mujer = +1


    while True:
        try:
            print("\n")
            edocivil=int(input("1.Soltero 2.Casado 3.divorciado 4.viuda:"))
            if edocivil in (1,2,3,4):
                break
            else:
                print("\n")
                print("ERROR")
        except ValueError:
            print("DATO ERRONEO.")


    match edocivil:
        case 1:
            Solterocont=+1

        case 2:
            casdocont=+1

        case 3:
            divorcidocont=+1

        case 4:
            viudacont=+1


    while True:
        try:
            print("\n")
            edad=int(input("Ingrese su edad (de 18 a 60):"))
            if edad >= 18 and edad <= 60:
                break
            else:
                print("ERROR")
        except ValueError:
            print("DATO ERRONEO.")

   




"""
ya despeus de este salto de liene se deja de repetir el ciclo
"""

print(f"la edad mayor de los hombres es de {edadmayorHombres}")
print(f"la edad menor de las muejeres cadas es de {mujeercasa}")
print(f"El porcentaje de los hombres divorciados es de: {hombre/divorcidocont*100}%")
print(f"El promedio de las mujeres casadas es de: {mujer/mujeercasa}")



se utulizara un ciclo for para soliciatar unos datos, los cuales son: 
El sexo de la perosona.
soltero , casado , divorciado , viuda .
ingresar la edad de entre 18 a 60

al finalizar el ciclo se mosrtrara por pantalla.

edad promedio de las mujeres casadas 
mayor edad de las muejeres
que porcentaje de los hombres estan divorcidos
menor edad de los hombres solteros

 python ./exercise/exer1.py
'''

edad=0

hombre=0
mujer=0

divorciados=0
casados=0

edadacun=0
edadcont=0
edadmayor=0


while True:
    try:
         nperson=int(input("Cuntas personas se registraran hoy ? :"))
         if   nperson < 1:
              print("ERROR. Dato menor que cero.")  
         else:
              break
    except ValueError:
         print("ERROR. Dato erroneo.")

# Declaramso el rango al caul va ir, como nunca se mostrara el dato final hay que sumarle uno al dato ingresado
for n in range (1, nperson+1):
     print('\n')
     while True:
          try:
               sexo=int(input(""" 
                              Ingrese su sexo: 
                              1.) Hombre
                              2.) Mujer
                              \n
                              Opciones (1 o 2):"""))
               if sexo in (1,2):
                    break
               else:
                    print("ERROR. los datos no pertenecen a la selecion")
          except ValueError:
               print("ERROR. dato erroneo")
    
     while True:
          try:
               edad=int(input("\tIngrese su edad (entre 18 a 60): "))
               if edad >=18 and edad <=60:
                    edadcont+=1
                    break
               else:
                    print("ERROR. Esta fuera de los limites dictaminados")
          except ValueError:
               print("ERROR. Dato erroneo.")
           
               
     while True:
          try:
               estado=int(input(""" 
                                Ingrese su estado civil:
                                1.)Soltero/a
                                2.)Divorciado/a
                                3.)Casada/o
                                4.)Viuda/o
                                \n
                                De las Cuatros opciones seleccione Una de ellas: """))
               if estado in (1,2,3,4):
                    break
               else:
                     print("ERROR. Esta fuera de los limites dictaminados")      
          except ValueError:
               print("ERROR. Dato erroneo.")

     print("\n")
     match sexo:
          case 1:
               hombre+=1
          case 2:
               mujer+=1
               if edad >= 30:
                    edadmayor+=1
             
     
                 
                
               
    
     match estado:
          case 1:
               if edad <=29:
                    solteros=+1
               
          case 2:
               if hombre >= 1:
                    divorciados+=1
          case 3:
               if mujer >= 1:
                    edadacun+=edad             
                           
               
               
        
        
try:
     print(f"El promedio de las edades de las muejeres casadas es de {format(edadacun/edadcont)}")
except ZeroDivisionError:
     print("Ha surgido un error al mometo de mostrar el promedio de las muejeres casadas. Division entre zero.")


print(f"La cantidad de muejeres mayores de 30 hacia adelante es de : {edadmayor}")
    
print(f"El porcentaje de los hombres divorciado es de: {(hombre/divorciados)*100}%")

print(f"La cantidad de hombres menores y solteros es de {solteros}")              
             

# print(f"El ciclo for se repito: {n} veces.")

          

     