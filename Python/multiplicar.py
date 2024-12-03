import random as r 

def calculo(n1,n2,res):
    return res == (n1 * n2)
    
n1 = r.randint(1,10)
n2 = r.randint(1,10)
continuar = True
while(continuar):
    res = int(input(f"Cuanto es {n1} * {n2} : "))
    if calculo(n1,n2,res):
        print("Enhorabuena!")
        continuar = False
    else:
        print("Paquete, repitelo!")

calculo(n1,n2,res)