
def es_triangulo_rectangulo(a, b, c):
    lados = sorted([a, b, c])
    return lados[0]**2 + lados[1]**2 == lados[2]**2

A = float(input("Ingresa el valor del lado A: "))
B = float(input("Ingresa el valor del lado B: "))
C = float(input("Ingresa el valor del lado C: "))

if A == B == C:
    print("El triángulo es equilátero.")
elif es_triangulo_rectangulo(A, B, C):
    print("El triángulo es rectángulo.")
elif A == B or B == C or A == C:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
