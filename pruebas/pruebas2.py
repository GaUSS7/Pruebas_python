x=3 #  se hace la variable global
def suma(): # se creae una fucnion que haga una suma con la variable que es global   
    global x # se decalrar la global, todas las variabales con el mismo nombre, "x" ahora responden a la variable global
    x=3+x # se suma la variable con 3, para luego ser actualizada, ya no es 3,ahora es 6
    print("EL resultad de la funcion suma es: ", x) #Me imprime el valor el resultaddo de la suma

suma()#llamo a la funciom para que se ejcute
print(x)# y tambien imprimo la variable global ya acutalizada, ahora es 6

def main():#creo una funcion main que tenga la funcion suma, para mostrar todo en una sola linea de codigo
    global x #hago la variable global, ahora todo que variable que sea "x" responden a la variable global con un valor de 6
    print(x)# La imprimo para mostrar el valor de la variable global, aun sigue siendo 6
    x=10+x# aqui la variable recibe el valor de 10+6=16, la variable global se actualiza, ya  no es 6, es 16
    suma()#vuelvo a llamar la funcion suma PERO, ahora tine el valor de 16, se hara la suma normal, sin ningun problema
    """PERO gracias a que la llame ahora la variable glogal se vuelve actualizar, y se hace la suma la funcion suma
    x=16+3=19, la variable global se actualiza, ya no es 16, es 19"""
    print("EL resultado de la funcion main es: ", x) #y ahora lo llamo con un print, el resultado que se supunia que tenia que manejar esta funcino
    """Ya no esta, ahora lo que esta llamadno la una variable global, es 19"""
    
   
print(x) 
main()
"""las funcinons se ejecutan o con paramtros, por omision o por llamda, el caso es que por cada vez que se llamen se van a a
a ejcutar, la funcion suma se llama dods veces, la primera sumando 3+3=6, luego se vuelve a llamar dentro de la funcin main
, pero la funcio main la 
acutilaizo la funcin global con un valor de 10+6=16 
para cuando se llame la funcion main, tambien se ejecuta la funcion suma, sumando 16+3=19
y por el pocionamiento del codigo, la funcicion suma actualiza la variable global con un valor de 19
y la funcin main la imprime"""
print(x) 

"""cada vez que se llama la funcion se hara lo que este  dentro de la funcion  
en este caso la variable x la volvemos global para que la pueda ser usada en la funcion main
y en la funcion suma"""

de=12
def suma2():
    global de
    de = 4+ de
    print(de)
    
def main2():
    global de
    de = 4 + de
    suma2()
    print(de)
    
    
main2()



"""Esta esta mal, la palabra reservada gloobal no peude ser inicializada dentro un fucnion con puras variable locales sin valor base
si bucas que el valor variable global tambien este dentro de la suma, tienes que ponerla  como global, en ambas funciones, porque 
toda variable que se inicialice dentro de una funion SON LOCALES"""
def suma3():
    global am
    am = 0
    am = 12 + am
    print(am)
    
def main3():
    am = 1
    am = 4 + am
    suma3()
    print(am)
    

main3()

lsits=[1,2,3,4,5,6]
print(2 in lsits)