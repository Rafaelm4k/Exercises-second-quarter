numero = int(input("Ingrese un numero: "))
if numero < 0:
    numeroPos = numero * -1
    print(f"El numero tiene {len(str(numeroPos))} cifras")
else:
    print(f"El numero tiene {len(str(numero))} cifras ")

