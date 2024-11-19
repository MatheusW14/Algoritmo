def numero_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:  
            return False
    return True

def intervalo_num_primos(inicio, fim):
    primos = [] 
    for num in range(inicio, fim + 1):  
        if numero_primo(num):
            primos.append(num)  # adiciona o número primo à lista
    return primos


inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

primos = intervalo_num_primos(inicio, fim)

print(f"Os números primos que estão no intervalo são: {primos}")
