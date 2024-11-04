Nomnreproducto = ["Manzana", "Banana", "Naranja"]
Precioprodito = [1.0, 0.5, 0.75]
Canntidadproducto = [100, 200, 150]

inventario = list(zip(Nomnreproducto, Precioprodito, Canntidadproducto))
print(inventario)

n=0
busquede=input("Ingrese el nombre del producto: ")
for producto, precio, cantidad in inventario:
    n+=1
    if producto == busquede:
            print( producto, precio, cantidad)
            nuevoPrecio = precio * (1 - 0.10 / 100)
            print(nuevoPrecio)
            precio[n] = nuevoPrecio
  
            
print(inventario)
   