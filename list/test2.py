estado = {
    "totlni": 0,
    "nvf": 0,
    "nv": 0,
    "mayPr4x4": 0,
    "SumCarga": 0,
    "CantidadCarga": 0,
    "porcentajeFamiliares": 0,
    "promedio": 0
}

def validarp(mensaje,precios=0):
    while True:
        try:
            precios=float(input(mensaje))
            if precios>=500:
                estado["totlni"]+=precios 
                return  precios 
            else:
                print("El precio esta por debajo de lo solicitado. (mayor o igual 500)")
        except ValueError:
            print("DATO ERRONEO.")

def validarTip(mensaje,tipos=0):
    while True:
        try:
            tipos=int(input(mensaje))
            if tipos == 1:
                print("Tipo de vehiculo selecionado: Familiar")
                estado["nvf"]+=1
                return 0.30
            elif tipos == 2:
                print("Tipo de vehiculo selecionado: 4x4")
                return 0.40
            elif tipos == 3:
                print("Tipo de vehiculo selecionado: Carga")
                return 0.60
            elif tipos ==4:
                return 4
            else:
                print("FUERA DE LOS LIMITES SOLICITADOS")
        except ValueError:
            print("DATO ERRONEO")


def calculos(tipos_vehiculos,precio):
    if tipos_vehiculos == 0.30:
        Vehiculo=("Familiar")
        estado["nvf"]+=1
        PrecioV=precio/tipos_vehiculos
    elif tipos_vehiculos == 0.40:
        Vehiculo=("4x4")
        PrecioV=precio/tipos_vehiculos
        if PrecioV > precio:
            estado["mayPr4x4"]=PrecioV

    elif tipos_vehiculos == 0.60:
        Vehiculo=("Carga")
        PrecioV=precio/tipos_vehiculos
        estado["SumCarga"]+=PrecioV
        estado["CantidadCarga"]+=1
        if estado["CantidadCarga"]>0:
            estado["promedio"]= estado["SumCarga"]/estado["CantidadCarga"]
        

    saldo=PrecioV-precio
    interes=saldo*0.20
    cuota=(saldo+interes)/24
    print(f""" 
          ******************************
          Tipos de Vehiculo: {Vehiculo} 
          Precio: {PrecioV} 
          Inicial: {precio} 
          Saldo: {saldo} 
          Interes: {interes} 
          Cuota: {round(cuota,2)}
          ***************************** 
          """)
    estado["nv"]+=1
    estado["porcentajeFamiliares"]= (estado["nvf"] * 100) / estado["nv"]
    




  
        

while True:
    print("""Seleecione el vehiculo que usted desea: 
      1)Familiar    30%
      2)4x4         40%
      3)Carga       60%
      4)Salir(opcion del programa)
      """)
    tipo=validarTip("Sellecione el tipo de vehiculo que usted desea: ")
    if tipo == 4:
        break
    pago=validarp("Ingrese el pago por el vehiculo que desea: ")
    calculos(tipo,pago)
    


print("Total Ingresado:", estado["totlni"])
print("Número de vehículos familiares:", estado["nvf"])
print("Número total de vehículos:", estado["nv"])
print("Mayor precio 4x4:", estado["mayPr4x4"])
print("Suma carga:", estado["SumCarga"])
print("Cantidad de carga:", estado["CantidadCarga"])
print("Porcentaje de familiares:", estado["porcentajeFamiliares"])
print("Promedio de carga:", estado["promedio"])


