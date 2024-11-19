def contar_caracteres(frase):
    contador = {}  
    for caractere in frase:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1
    return contador


frase = input("Digite uma frase: ")

resultado = contar_caracteres(frase)

print("Contagem de caracteres:")
for caractere, quantidade in sorted(resultado.items()): # O sorted coloca a contagem dos itens em ordem alfabética (Separando as maiúsculas das minúsculas).
    print(f"'{caractere}': {quantidade}")               #.items() acessa a chave e o valor de cada item do dicionário.
    
