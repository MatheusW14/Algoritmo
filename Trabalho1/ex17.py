def ordenar_negativos_positivos(lista):
    negativos = [x for x in lista if x < 0]
    positivos = [x for x in lista if x >= 0]
    return negativos + positivos

entrada = input("Digite os números separados por espaço: ").split()
numeros = []  


for num in entrada:
    numeros.append(int(num))

resultado = ordenar_negativos_positivos(numeros)

print(f"Lista ordenada: {resultado}")