def conversor_temperatura(C):
    return C * 1.8 + 32

C = float(input("Digite a temperatura em Graus Celcius:"))

resultado = conversor_temperatura(C)
print(f"A temperatura {C}°C corresponde a {resultado}°F.")

