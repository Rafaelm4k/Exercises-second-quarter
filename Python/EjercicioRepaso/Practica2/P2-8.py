continuar = True
n = int(input("Ingresa un numero : "))
while(continuar):
    fallos = 0
    for i in range(10):
        calcular = int(input(f"Cuanto es {n} x {i+1} : "))
        if calcular == (n * (i+1)):
            print(f"Correcto.")
        else:
            print(f"Incorrecto.")
            fallos+=1
    salida=input("Desea Continuar ? S/N : ").upper()
    if salida == "N":
        continuar = False
        print(f"Fallaste {fallos} Veces")
    else:
        print(f"Siguiente tabla es la del {n+1}")
        print(f"Fallaste {fallos} Veces")
        n+=1