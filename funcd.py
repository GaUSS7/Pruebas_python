def validaraname():
    while True:
        name=input("Ingrese nomrbe: ")
        lis=name.split()
        v=True
        for a in lis:
            if not a.isalpha(): #ya el isalpha se trasnforma en bool, es redundate que se igual a true or false
                v=False
                break

        if v:
            return f"El nombre es: {name}"
        else:
            print("ERROR")
        
    


print(validaraname())







        
