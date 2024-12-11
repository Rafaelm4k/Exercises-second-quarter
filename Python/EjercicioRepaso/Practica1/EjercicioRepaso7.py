def bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

año = int(input("Ingrese el año: "))

if bisiesto(año):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

