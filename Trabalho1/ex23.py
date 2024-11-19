def somar_numeros(numero1, numero2):  
    return numero1 + numero2

def subtrair_numeros(numero1, numero2):  
    return numero1 - numero2

def multiplicar_numeros(numero1, numero2):  
    return numero1 * numero2

def dividir_numeros(numero1, numero2):  
    if numero2 == 0:
        return "Erro! Não é possível dividir por zero."
    return numero1 / numero2


print(f"Calculadora básica!")

num1 = float(input("Digite o primeiro número:"))  
num2 = float(input("Digite o segundo número:"))

operacao = input("Escolha a operação (adição(+), subtração(-), multiplicação(x), divisão(%)): ").lower()

if operacao == "adição" or "+":
    resultado = somar_numeros(num1, num2)
elif operacao == "subtração" or "-":
    resultado = subtrair_numeros(num1, num2)
elif operacao == "multiplicação" or "x":
    resultado = multiplicar_numeros(num1, num2)
elif operacao == "divisão" or "%":
    resultado = dividir_numeros(num1, num2)
else:
    resultado = "Operação inválida!"

print(f"O resultado da operação é: {resultado}")
