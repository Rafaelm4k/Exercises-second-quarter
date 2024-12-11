def organizarNumeros(numeros):
    return sorted(numeros)

numeros = []
for i in range(5):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)

print(f"Los numeros ordenados son: {organizarNumeros(numeros)}")