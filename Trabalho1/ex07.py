def palavra_invertida(palavra):
    return palavra[::-1]

palavra = str(input(f"Digite uma palavra e iremos invertela:"))

resultado = palavra_invertida(palavra)

print(f"A palavra vira: {resultado}")