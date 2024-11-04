"""validar todo"""
"""
El departamento de recursos humanos de una empresa está solicitando un reporte y quiere visualizar los siguientes datos:
-Nombre del empleado
-Cédula del empleado
-Edad del empleado
-Tiempo en la empresa (años)
-Salario del empleado($ dos decimales)

El programa debe solicitar los datos a cada empleado hasta que se indique lo contrario,
al finalizar el programa ha de mostrar una tabla con encabezados coherentes, junto a todos los datos solicitados en orden

Se considera finalizado si tu programa puede mostrar en pantalla lo solicitado
Puedes tener un archivo de validaciones externo

"""
"""def validaTOdo(message,Max=0,Min=0):
     while True:
          try:
               numero=float(input(message))
               dato=len(str(numero)) #el str es para convertirlo en string y que lo cuente, el len es para saber cuantos digitos tiene
               print(dato)
               if Max != 0 and Min !=0:
                    if dato > Min and dato <= Max:
                         for a in str(numero): #no puede tener range porque no estoy contando las iteraciones estoy asignando datos, solo texto 
                              if a.isalpha():
                                   print("esta dentro de los paraemtros pero no es totalmenete numerico")
                                   break
                              else:
                                    return numero
                    else:
                         print("El numero no esta dentro de los parametros")
               else:
                    return numero
          except ValueError:
               print("El dato ingresado no es numerico")"""



def validarCedulaYedad(message,Max=0,Min=0): #esta funcion me esta validando casi todo
     while True:
               cedula=input(message)
               limitecedula=len(cedula)
               val=True
               if Max != 0 and Min !=0:
                    if limitecedula > Min and limitecedula <= Max:
                         for a in str(cedula):
                              if not(a.isdigit()):
                                   val=False
                                   print("El dato no es numerico")
                                   break                    
                    else:
                         print("El numero no esta dentro de los parametros")
                         val=False      
                    if val:
                         return cedula
               else:
                    return cedula
         
                
                              
def valdiraNane(message):
     while True:
          name=input(message)
          namePart=name.split(" ")
          val=True
          for a in namePart:
               if not(a.isalpha)():
                    print("El nombre tiende datos numericos. ERROR")
                    val=False
                    break
          if val:
               return name
     
       
      
reporte=[]        
while True:
     nombre=valdiraNane("Ingrese su nombre: ")
     print(nombre)

     cedula=validarCedulaYedad("Ingrese su cedula: ",10,7)
     print(cedula)
     edad=validarCedulaYedad("Ingrese su edad: ",100,1)
     print(edad)
     tiempo=validarCedulaYedad("Ingrese su tiempo en la empresa: ",100,1)
     print(tiempo)

     salario=validarCedulaYedad("Ingrese su Salario: ",100,1)
     salariun=round(float(salario),2)
     print(salariun)

     reporte.append([nombre,cedula,edad,tiempo,salariun])
     print(reporte)
     
     continuar=input("Desea ingresar otro empleado? Y/N: ")
     if continuar in ("n","N"):
          break


#listas anidadas pero con todo la inforamcion en jun solo espacio to

for n in (reporte): #me muestra el reporte:
          print(f"""
          Nombre: {n[0]}
          Cedula: {n[1]}
          Edad: {n[2]}
          Tiempo en la empresa: {n[3]}
          Salario: {n[4]}
          *************************
          """)
         
     
