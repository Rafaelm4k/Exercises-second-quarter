continuar = True
n = int(input("Ingresa un numero : "))
while(continuar):
    for i in range(10):
        calcular = int(input(f"Cuanto es {n} x {i+1} : "))
        if calcular == (n * (i+1)):
            print(f"Correcto.")
        else:
            print(f"Incorrecto.")
    salida=input("Desea Continuar ? S/N : ").upper()
    if salida == "N":
        continuar = False
    else:
        print(f"Siguiente tabla es la del {n+1}")
        n+=1