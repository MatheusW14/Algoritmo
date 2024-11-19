# Função para contar palavras únicas
def contar_palavras_unicas(texto): 
    palavras = texto.split()
    palavras_unicas = set(palavras) #função set não permite duplicatas.
    return len(palavras_unicas) 

texto = input("Digite um texto para contar as palavras únicas: ")

resultado = contar_palavras_unicas(texto)

print(f"O número de palavras únicas é: {resultado}")
