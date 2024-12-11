import math
numero = int(input("Ingrese un numero: "))

if numero < 0:
    print("¡ERROR!, El numero es negativo")
else:
    print(f"La raiz cuadrada es {math.sqrt(numero)}")