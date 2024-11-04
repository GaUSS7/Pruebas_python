"""            MAteriales            precios         stock"""
"""#a=[["zapato","pantalon","camisa"],[34.3,12.3,12.3],[20,10,5]]
print(a[-1][0])# posicion de las listas negativas
ver poscion de listas anidadas print(nombrelista[poscion de la lista principal][poscion de la lista anidada])
for index in a:
    print(index[0] , index[1] , index[2])"""
    
    
#listas anidadas pero con la informacion en otros epoacios de la lista
Nombres=["zapato","pantalon","camisa"]
Precios=[34.3,12.3,12.3]
Stock=[20,10,5]

union = list(
    zip(
        Nombres,
        Precios,
        Stock)
    )

for elemneto in union:
    print(elemneto)
    
for nomrbes,perecios,stocks in union:
    print(f"""El nombre es: {nomrbes} el precio es: {perecios} el stock es: {stocks}""")
    
    
print("\n")


for nomrbes,perecios,stocks in zip(Nombres,Precios,Stock):
    print(f"""El nombre es: {nomrbes} el precio es: {perecios} el stock es: {stocks}""")
    
    
apellidos=[]
capital=[]
nacimiento=[]
while True: 
     ape=input("apellido: ")
     capi=input("capital: ")
     nac=input("nacimiento: ")
     
     apellidos.append(ape)
     capital.append(capi)
     nacimiento.append(nac)
     
     continuar=input("Desea ingresar otro empleado? Y/N: ")
     if continuar in ("n","N"):
          break
  
    
print(apellidos)
print(capital)
print(nacimiento)
unnon = list(zip(apellidos,capital,nacimiento))

for n,c,na in unnon:
    print(f"""
          Apellidos:{n}
          Capital:{c}
          Nacimiento:{na}
          ********************
          """)

"""La funcion zip se usa para unir dos o mas listas la iteracion va de la mano con las listas que unas, por cada iteracion 
que haga mostrar el espaccio 0 de cada uno de ellos, tomanr en cuenta  que la funcin zip solo ietara hasta el menor mas cercano
osea, que si hay una lista de 10 y una de 5, va a iterar 5 veces dejando las demas"""
     
      