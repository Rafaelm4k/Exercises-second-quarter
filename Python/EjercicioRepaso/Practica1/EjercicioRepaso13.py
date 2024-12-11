numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
calcular = input("Que operacion desea realizar SUMA/RESTA/MULTIPLICACION/DIVISION: ").upper()

if calcular == "SUMA":
    print(f"El resultado es {numero + numero2}")
elif calcular == "RESTA":
    print(f"El resultado es {numero - numero2}")
elif calcular == "MULTIPLICACION":
    print(f"El resultado es {numero * numero2}")
elif calcular == "DIVISION":
    print(f"El resultado es {numero / numero2}")
