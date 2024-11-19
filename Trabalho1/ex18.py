def receber_matriz():
    n = int(input("Digite o tamanho da matriz quadrada(n x n): "))  
    matriz = []

    for i in range(n):
        print(f"Digite os números da linha {i + 1}, separados por espaço:")
        linha = input().split()  
        linha = [int(num) for num in linha]  
        matriz.append(linha)
    return matriz

def somar_diagonais(matriz):
    soma_principal = 0
    soma_secundaria = 0
    n = len(matriz)

    for i in range(n):
        soma_principal += matriz[i][i]  # adiciona os elementos [0][0], [1][1], [2][2] da matriz.
        soma_secundaria += matriz[i][n - 1 - i]  # coluna=n−1−i, onde 'n' é o tamanho da matriz (número de linhas ou colunas) e 'i' é o índice da linha atual no loop.
    return soma_principal, soma_secundaria

matriz = receber_matriz()
soma_principal, soma_secundaria = somar_diagonais(matriz)

print(f"\nA matriz digitada foi:")
for linha in matriz:
    print(linha)

print(f"\nSoma da diagonal principal: {soma_principal}")
print(f"Soma da diagonal secundária: {soma_secundaria}")
