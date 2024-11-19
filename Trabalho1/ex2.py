def verificacao_par_ou_impar(numero):
    if numero % 2 == 0: 
        return "Par"
    else:
        return "Ímpar"
    
print("Verifique se o número é par ou ímpar:")
numero = int(input("Digite um número: "))

resultado = verificacao_par_ou_impar(numero)
print(f"{numero} é {resultado}.") 