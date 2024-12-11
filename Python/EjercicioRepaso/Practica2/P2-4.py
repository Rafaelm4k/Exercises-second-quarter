import math
continuar = True
while(continuar):
    numero = int(input("Ingrese un numero : "))
    if numero > 0 :
        print(f"la raiz cuadrada de {numero} es {math.sqrt(numero)}")
        continuar = False
    else:
        print(f"{numero} es un numero negativo, Debes ingresar uno positivo")
