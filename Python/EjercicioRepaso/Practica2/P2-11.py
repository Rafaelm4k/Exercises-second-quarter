def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2 
    
    return binario


numero_decimal = int(input("Ingresa un número decimal positivo: "))
binario = decimal_a_binario(numero_decimal)
print(f"El número binario es: {binario}")
