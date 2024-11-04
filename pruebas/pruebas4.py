

inventario=[]





def aplicar_descuentoor_incremento(mesaje,inventarios):
    while True:
        busqerda=input(mesaje)
        for Nam , Pre , Canm in inventarios:
            n+=1
            if Nam == busqerda:
                    print( Pre,  Pre, Canm)
                    nuevoPrecio = Pre * (1 - 0.10 / 100)
                    print(nuevoPrecio)
                    Pre[n] = nuevoPrecio
                
                
    
        
        
        
    







while True:
    print("Bienvenido al inventario")
    nameproduc=input("Ingrese el nombre del producto: ")
    print("\n")
    pricepruduct=float(input("Ingrese el precio del producto: "))
    print("\n")
    amountproduct=int(input("Ingrese la cantidad del producto: "))
    
    inventario.append([nameproduc,pricepruduct,amountproduct])
    
    print("\n")
    continuar=input("Desea agregar otro producto? Y/N: ")
    if continuar in ("n","N"):
        break

for Nam , Pre , Canm in inventario:
    print(f"""
          *************************
          Nombre del producto: {Nam}
          Precio del producto: {Pre}
          Cantidad del producto: {Canm}
          *************************
          """)
    print("\n")
    
    while True:
        descuento=input("Desea aplicar algun descuento o Incremento? Y/N: ")
        if descuento in ("n","N"):
            break
        else:
            aplicar_descuentoor_incremento("Descuento o Incremento : ",inventario)
           
          
            
            
        