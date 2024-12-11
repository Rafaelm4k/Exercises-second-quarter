nota = float(input("Ingrese la nota: "))
edad = int(input("Ingrese la edad: "))
genero = input("Ingrese el genero F/M : ").upper()

if nota >= 5 and edad >= 18 and genero == "F":
    print("Aceptada")
elif nota >= 5 and edad >= 18 and genero == "M":
    print("Aceptado")
else:
    print("No Aceptado/a")

