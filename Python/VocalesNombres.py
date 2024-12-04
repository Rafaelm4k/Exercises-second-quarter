n = int(input("Cuantos nombres quieres ingresar ? : "))
nombres = []
contador = []
vocales = ['a', 'e', 'i', 'o', 'u']

def calculo(nombres,contador):
    for i in range(len(nombres)):
        suma = 0
        palabra = nombres[i]
        for j in range(len(palabra)):
            if palabra[j] in vocales:
                suma += 1
        contador.append(suma)
    return contador
    
for i in range(n):
    nombre = input(f"Ingresa el nombre nª {i+1} : ").lower()
    nombres.append(nombre)
calculo(nombres,contador)

for i in range(len(nombres)):
    print(f"El nombre de {nombres[i]} tiene {contador[i]} Vocales.")

print("Ejercicio realizado por rf_jr")
