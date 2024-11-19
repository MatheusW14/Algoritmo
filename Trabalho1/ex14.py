def palavra_invertida(palavra):
    if palavra[::-1] == palavra:
        return True
    else:
        return False

palidromo = str(input(f"Verifique se a palavra é um políndrono (ou seja, se lê igual de trás para frente): "))

resultado = palavra_invertida(palidromo)

if resultado == True:
    print(f"A palavra é um palídromo.")
else:
    print(f"A palavra não é um palídromo.")
