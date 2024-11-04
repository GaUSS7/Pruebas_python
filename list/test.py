"""Ejercicio: Simulador de Cuenta Bancaria
Crea un programa que permita al usuario realizar operaciones bancarias básicas usando variables globales. 
El programa debe tener las siguientes funciones:

consultar_saldo(): Imprime el saldo actual de la cuenta.
depositar(cantidad): Aumenta el saldo de la cuenta en la cantidad especificada.
retirar(cantidad): Disminuye el saldo de la cuenta en la cantidad especificada, si hay suficiente saldo.
menu(): Presenta al usuario un menú para realizar las operaciones disponibles.
Requerimientos:

Usa una variable global saldo para almacenar el saldo de la cuenta.
Utiliza funciones que modifiquen y lean el valor de saldo."""

#el saldo debe ser global
global saldo
saldo =0



def validarlimit(mesege,min=0,max=4):
    while True:
        try:
           show=int(input(mesege))
           if show<=min or show>max:
              print("ERROR.opcion incorrecta.")
           else:
              return show   
        except ValueError:
           print("ERROR DATO")
        

def validarcantidad(message):
   while True:
      try:
         cantidad=float(input(message))
         if cantidad >=0:
            return cantidad
         else:
          print("ERROR, numeors negativo")
      except ValueError:
         print("Dato erroneo")
      
   
  
def validarlimt(message):
   global saldo
   while True:
      try:
         cantid=float(input(message))
         if cantid < 0 or cantid > saldo:
            print("NO puede retirar una cantidad que no tiene")  
         else:
            return cantid 
      except ValueError:
         print("ERROR")




def consultar_saldo():
   print(f"El saldo en estos momentos de tu cuenta es de: {saldo}")
   

def depositar(cantidad):
    global saldo #decirle que es un dato global
    saldo += cantidad
   

def retirar(cantidad):
   global saldo
   saldo -= cantidad
   return saldo
 
   
      
   



def menu():
     while True:
         print("""Opcioens del Benco: \n
          1)Consultar su saldo.
          2)Depositar Cantidad.
          3)Retirar Cantidad.
          4)Salir \n
          """)
         options=validarlimit("Seleccione una de las 4 opciones: ")
         match options:
            case 1:
               print('Consultar su saldo a la cuneta del banco')
               consultar_saldo() 

            case 2:
                print('Depositar dinero a la cuenta del banco.')
                cantidad=validarcantidad("Cuanto desea depositar: ")
                depositar(cantidad)
                print(f"Se deposito una cantidad de: {cantidad} $") 

            case 3:
               print('Retirar Cantidad de la cuenta del banco')
               print(f"Su saldo es de: {saldo} $")
               if saldo <=0:
                  print("saldo insuficiente.")
               else:
                  cantidad=validarlimt("Cuanto va a retirar de su saldo actual: ")
                  print(f"Usted esta retirando {cantidad} de un saldo de {saldo}")
                  resto=retirar(cantidad)
                  print("le queda",resto) 
            case 4:
               break 
     
    


menu()

"""Los datos tipos strnig no se llevan con los calucilos, evitar los errores con try expect"""
