import random as r
aleatorio = r.randint(1,100)
continuar = True

while(continuar):
    adivinar = int(input("Ingresa un numero : "))
    if adivinar == aleatorio:
        print("Correcto!")
        continuar= False
    else:
        if adivinar > aleatorio:
            print("El numero es Menor")
        else: 
            print("El numero es Mayor")