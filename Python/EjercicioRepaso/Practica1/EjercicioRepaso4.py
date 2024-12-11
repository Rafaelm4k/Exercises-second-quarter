base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
exponentePos =  exponente * -1

if exponente > 0:
    print(f"La potencia de {base} elevada a {exponente} es {base ** exponente}")
elif exponente < 0:
    print(f"La potencia de {base} elevada a {exponente} es {1/(base ** exponente)}")
elif exponente == 0:
    print("La potencia es 1")

