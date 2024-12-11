continuar = True
continuar2 = True
n = int(input("Ingresa un numero : "))
while(continuar):
    fallos = 0
    tabla = 1
    while(continuar2):
        if tabla == 11:
            continuar2 = False
        else:
            calcular = int(input(F"Cuanto es {n} x {tabla} : "))
            if calcular == (n*tabla):
                print("Correcto")
                tabla+=1
            else:
                print("Incorrecto")
                tabla+=1
                fallos+=1
                if fallos == 2:
                    print("Haz tenido 2 Fallos, Te toca responder la tabla de nuevo. ")
                    tabla = 1
            
    salida=input("Desea Continuar ? S/N : ").upper()
    if salida == "N":
        continuar = False
        print(f"Fallaste {fallos} Veces")
    else:
        print(f"Siguiente tabla es la del {n+1}")
        print(f"Fallaste {fallos} Veces")
        n+=1