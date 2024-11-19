def somar_numeros(numero1, numero2):  
    return numero1 + numero2

print(f"Calculadora de soma!")

num1 = float(input("Digite o primmeiro número:"))  
num2 = float(input("Digite o segundo número:"))

resultado = somar_numeros(num1, num2)
print(f'A soma dos números é: {resultado}')