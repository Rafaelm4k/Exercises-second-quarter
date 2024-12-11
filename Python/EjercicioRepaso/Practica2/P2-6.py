continuar = True
positivo = 0 
negativo = 0
cero = 0
while(continuar):
    numero = int(input("Ingrese un numero: "))
    if numero > 0: 
        positivo+=1
    elif numero == 0:
        cero+=1
    else:
        negativo+=1 

    salida = input("Deseas Continuar? S/N : ").upper()
    if salida == "N":
        continuar = False

print(f"Ingresaste {positivo} numeros positivos")
print(f"Ingresaste {negativo} numeros negativos")
print(f"Ingresaste {cero} numeros iguales a cero")