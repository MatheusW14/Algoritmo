def filtro_pares_na_lista(lista):
    lista_pares = []
    for num in lista:
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares

entrada = input("Digite uma lista de números inteiros, separados por espaço: ")

lista = [int(x) for x in entrada.split()]

resultado = filtro_pares_na_lista(lista)

print(f"A lista de pares é: {resultado}")
