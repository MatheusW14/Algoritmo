def numeros_lista(lista):
    return len(lista)

print("Digite os números para a lista, separados por espaço:")
entrada = input()

lista = [float(num) for num in entrada.split()]

print(f"Sua lista tem {numeros_lista(lista)} números.")