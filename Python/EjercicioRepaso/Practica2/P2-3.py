n = int(input("Ingresa un numero : "))

for i in range(10):
    calcular = int(input(f"Cuanto es {n} x {i+1} : "))
    if calcular == (n * (i+1)):
        print(f"el resultado de {n} x {i+1} es Correcto.")
    else:
        print(f"el resultado de {n} x {i+1} es Incorrecto.")