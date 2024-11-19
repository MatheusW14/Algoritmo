def mesclar_dicionarios(dicionario1, dicionario2):
    fusao_dicionario = {}

    for chave, valor in dicionario1.items():
        fusao_dicionario[chave] = valor
    
    for chave, valor in dicionario2.items():
        if chave in fusao_dicionario:
            fusao_dicionario[chave] += valor
        else:
            fusao_dicionario[chave] = valor
    return fusao_dicionario

# exemplos de dicionários
dicionario1 = {'a': 10, 'b': 20, 'c': 30}
dicionario2 = {'b': 5, 'c': 10, 'd': 40}


resultado = mesclar_dicionarios(dicionario1, dicionario2)

print(f"Dicionário mesclado: {resultado}")
