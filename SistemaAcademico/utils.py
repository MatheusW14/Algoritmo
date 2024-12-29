def obter_entrada(prompt, validacao=None, erro="Entrada inválida. Tente novamente."):
    """
    Solicita uma entrada do usuário e a valida.

    Args:
        prompt (str): A mensagem a ser exibida ao solicitar a entrada.
        validacao (callable, optional): Uma função que valida a entrada. Deve retornar True se a entrada for válida.
        erro (str, optional): A mensagem de erro a ser exibida se a entrada for inválida.

    Returns:
        str: A entrada válida do usuário.
    """
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
