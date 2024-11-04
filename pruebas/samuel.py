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

logros:
    * No-Fail (codigo 100% validado)
    * ??? (Optimus Prime)
    * Impecable (Los elementos de tu salida son agradables y están centrados)
    * ??? (son las 1500 horas)
    * ??? (la Rae estaría orgullosa)
    * Soy el python (Haz todos los logros)
"""

#functions

def validnamelastname(message):
    while True:
        lastnameandname=input(message)
        chop=lastnameandname.split(" ")
        if all(parte.isalpha() for parte in chop):
            return lastnameandname
        else:
            print("El nombre tiene datos numericos. ERROR")
#esta  funcion valida nombres y apellidos       

def validName(message):
    while True:
        names=input(message)
        if names.isalpha():
            return names
        else:
            print("El nombre tiene datos numericos. ERROR")
#esta funcion valida solo nombres
            
def validCEDU(message,Max=0,Min=0,Error=0):
    while True:
        cedula=input(message)
        limitecedula=len(cedula)
        if limitecedula > Min and limitecedula <= Max:
            if cedula.isdigit():
                return cedula
            else:
                print("El dato no es numerico")
        else:
            print(Error)
#esta funcion valida solo cedulas,edad y tiempo de trabajo
            
def Validarsalaty(message):
    while True:
        try:
            salariun=float(input(message))
            if salariun <0:
                print("El salario no puede ser negativo")
            else:
                return salariun
        except ValueError:
            print("Dato erroneo")
#esta funcion valida solo salarios
    
    
    
                
        
       
            
        
        




#main
empleados=[]

while True:
    
    name=validnamelastname("Ingrese el nombre del emmpleado: ")
    CEDEu=validCEDU("Ingrese la cedula del empleado: ",10 , 7, "La cedula no puede ser menor a 7 o mayor a 10")
    age=validCEDU("Ingrese la edad del empleado: " ,3,1, "La edad no puede ser menor de  1")
    buisness=validCEDU("Ingrese el tiempo en la empresa: ", 3, 1, "El tiempo no puede ser menor de 1")
    salary=Validarsalaty("Ingrese el salario del empleado: ")
    
    print("\n")
    
    empleados.append([name,CEDEu,age,buisness,salary])
    
    exiT=input("Desea agregar otro empleado? Y/N: ")
    if exiT in ("n","N"):
        break
    

print(empleados)
print("\n")
print("""
      Reporte de Empleados
      *************************""")
for inf in empleados:
    print(f"""
          Nombre del empleado: {inf[0]}
          Cedula del empleado: {inf[1]}
          Edad del empleado: {inf[2]}
          Tiempo en la empresa: {inf[3]}
          Salario del empleado: {round(inf[4],2)}
          \n
          """)
    