def verificar_linhas(tabuleiro):
    for linha in tabuleiro:
        if len(set(linha)) != 9:
            return False
    return True

def verificar_colunas(tabuleiro):
    for col in range(9):
        coluna = [tabuleiro[row][col] for row in range(9)] # row percorre as 9 linhas do tabuleiro (de 0 a 8), uma por vez.
        if len(set(coluna)) != 9: 
            return False
    return True

def verificar_subgrades(tabuleiro):
    for i in range(0, 9, 3):  # Itera sobre as subgrades 3x3
        for j in range(0, 9, 3):
            subgrade = []
            for x in range(3):
                for y in range(3):
                    subgrade.append(tabuleiro[i + x][j + y])
            if len(set(subgrade)) != 9:
                return False
    return True

def verificar_sudoku(tabuleiro):
    if verificar_linhas(tabuleiro) and verificar_colunas(tabuleiro) and verificar_subgrades(tabuleiro):
        return True
    else:
        return False

# exemplo de tabuleiro 
tabuleiro = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

if verificar_sudoku(tabuleiro):
    print("O tabuleiro de Sudoku é válido!")
else:
    print("O tabuleiro de Sudoku NÃO é válido!")
