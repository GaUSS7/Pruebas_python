def validarRango(mensaje, iz=0,
                 der=None):  # INTRODUCE EL RANGO IZQUIERDO, LUEGO EL DERECHO Y LUEGO EL MENSAJE QUE QUIERAS QUE SE REPRODUZCA
    while True:
        try:
            numero = float(input(mensaje))
            if der == None:
                if numero < iz:
                    print("el nuermo que ha ingresado no puede ser menor a ", iz)
                else:
                    return numero

            elif iz <= numero <= der:
                return numero
            else:
                print("El Numero está fuera de rango")
        except ValueError:
            print("Eso no es un numero")


sueldoMinimo = validarRango("Cual es el saldo minimo? (minimo 180)\n", 180)
empleados = 0
cantEmpleadosAumento = 0
aumentoSuma = 0
mayorSaldo = 0


def ajusteSueldo():
    global nuevoSueldo
    global aumento
    global aumentoSuma
    global cantEmpleadosAumento
    global mayorSaldo
    global cedulMayorSaldo
    aumento = 0

    if antiguedad > 2 or sueldoActual < sueldoMinimo:
        aumento = sueldoActual / 100 * 30

    nuevoSueldo = sueldoActual + aumento

    if nuevoSueldo < sueldoMinimo:
        aumento = aumento + (sueldoMinimo - nuevoSueldo)
        nuevoSueldo = sueldoMinimo

    if aumento != 0:
        aumentoSuma += aumento
        cantEmpleadosAumento += 1
        if mayorSaldo < nuevoSueldo:
            mayorSaldo = nuevoSueldo
            cedulMayorSaldo = cedula


while True:
    cedula = validarRango("Ingrese su cedula (7-8 caracteres)\n", 1000000, 99999999)
    antiguedad = validarRango("Ingrese su antiguedad en la empresa en años\n")
    sueldoActual = validarRango("ingrese su sueldo actual, debe ser mayor a 130\n", 130)
    ajusteSueldo()

    empleados += 1
    print(f"""
    *******************************
    *Cédula: {cedula}
    *Antiguedad: {antiguedad} años
    *Sueldo Actual: {sueldoActual} bs
    *Aumento: {aumento} bs
    *Nuevo Sueldo: {nuevoSueldo} bs
    *******************************""")
    resp = input("Desea Procesar otro empleado? Y/N\n")
    if resp in ("n", "N"):
        break
porcEmpleadosAumento = cantEmpleadosAumento * 100 / empleados
print(f"""
*******************************
*La nomina se incrementó en: {aumentoSuma}
*Cantidad de empleados procesados: {empleados}
*Cantidad de empleados con aumento: {cantEmpleadosAumento}
*Porcentaje de empleados con aumento: {round(porcEmpleadosAumento, 2)}%
*El mayor saldo luego del aumento fue  de {mayorSaldo} y lo recibió la cedula: {cedulMayorSaldo}
*******************************""")
