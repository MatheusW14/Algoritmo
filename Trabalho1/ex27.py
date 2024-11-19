def contar_frequencia(texto):
    palavras = texto.lower().split()
    
    frequencia = {}
    
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

def palavras_mais_frequentes(frequencia):
    palavras_ordenadas = sorted(frequencia.items(), key=lambda x: x[1], reverse=True) 
    return palavras_ordenadas[:5]
# o lambda x: x[1] recebe o item de frequencia.itens() e retorna o segundo elemento, no caso a frequencia, e o reverse=True, alinha em forma decrescente.

texto = input("Digite um texto longo: ")


frequencia = contar_frequencia(texto)


top_5_palavras = palavras_mais_frequentes(frequencia)


print("As 5 palavras mais frequentes no texto são:")
for palavra, contagem in top_5_palavras:
    print(f"Palavra: '{palavra}' - Frequência: {contagem}")
