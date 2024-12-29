
def obter_entrada(prompt, validacao=None, erro="Entrada inválida. Tente novamente."):
    while True:
        entrada = input(prompt).strip()
         # Verifica se há validação e se a entrada é válida
        if validacao:
            if validacao(entrada):
                return entrada
            else:
                print(erro)
        elif entrada:  # Se não houver validação, apenas verifica se não está vazia
            return entrada
        else:
            print(erro)
