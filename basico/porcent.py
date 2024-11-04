'''Vas a caulcular el porcentaje de un dato el caul vas a pedir, lo haras con los dos ciclos que tiene python'''
personaMENOR=0
personaMAYOR=0
hombres=0
mujeres=0
total=0

while True:
    
    personas=int(input("Cuantos anios tines: "))
    genero=int(input("Que sexo es usted ?: (1) para nombres y (2) para mujeres. /n"))
    
    if personas >=25:
        personaMAYOR+=1
    else:
        personaMENOR+=1

    if genero == 1:
        hombres+=1
    elif genero == 2:
        mujeres+=1

    total+=1 #las peronas que van ingresando
    continuar=int(input("Dese volverlo a repetir: (1) Si y (2) No  \n"))
    if continuar == 2:
        break
    

print('\n')
personasMpor= (personaMAYOR*100) / total
pors=round(personasMpor,2)

personasMEpor= (personaMENOR*100) / total
psor=round(personasMEpor,2)

'''Porcentaje de hombres y muejeres.'''
hombrepor =(hombres*100)/total
hom=round(hombrepor,2)

mujerespor =(mujeres*100)/total
munn=round(mujerespor,2)

print(f"el total de peroans registrasdas fue de: {total}")
print('\n')
print(f'''El porcentjae de los hombres y las mujeres son:
      La cantidad de hombres fueron {hombres} y muejeres fueron {mujeres} 
      Porcentaje de los hombres: {hom}% 
      Porcentaje de las muejeres: {munn}% \n
     ''')
print(f''' El porcentaje de las peronas de mayor y menor edad son:
      La cantidad de mayores de edad fueron {personaMAYOR} y menores fueron {personaMENOR} 
      Porcentaje de los mayores de edad: {pors}%
      Porcentaje de los menores de edad: {psor}%''')