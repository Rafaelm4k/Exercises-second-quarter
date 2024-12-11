numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

numeroMayor = numero if numero > numero2 else numero2
numeroMenor = numero if numero < numero2 else numero2

print(f"El numero mayor es {numeroMayor} y el numero menor es {numeroMenor}")