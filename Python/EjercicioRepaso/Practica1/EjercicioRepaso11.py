numero = []
for i in range(3):
    numero.append(int(input("Ingrese un numero: ")))
print(f"los numeros ordenados de mayor a menor son: {sorted(numero, reverse=True)}")