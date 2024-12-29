import random
import string
from utils import obter_entrada

alunos = []


def gerar_matricula():
    numero = random.randint(1, 9999)
    letra = random.choice(
        string.ascii_uppercase
    )  # random.choice() escolhe um único elemento aleatório de uma sequência (lista, tupla, string, etc.).
    matricula = f"{numero:04}{letra}"
    return matricula


def cadastrar_aluno():
    """
    Cadastra um novo aluno no sistema.
    """
    matricula = gerar_matricula()

    campos = [
        ("Digite o nome do aluno:", str),
        (
            "Digite a data de nascimento (DD/MM/AAAA):",
            lambda x: len(x) == 10 and x[2] == "/" and x[5] == "/",
        ),
        ("Digite o sexo (M/F):", lambda x: x in ["M", "F"]),
        ("Digite o endereço:", str),
        ("Digite o telefone (apenas números):", lambda x: x.isdigit()),
        ("Digite o email:", str),
    ]

    respostas = []
    for campo, tipo in campos:
        resposta = obter_entrada(campo, validacao=tipo)
        respostas.append(resposta)

    aluno = {
        "nome": respostas[0],
        "matricula": matricula,
        "data_nascimento": respostas[1],
        "sexo": respostas[2],
        "endereco": respostas[3],
        "telefone": respostas[4],
        "email": respostas[5],
    }

    alunos.append(aluno)
    print(f"Aluno {aluno['nome']} cadastrado com sucesso!\n")


def listar_alunos():
    """
    Lista todos os alunos cadastrados.
    """
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
    else:
        print("\n=== Lista de Alunos ===")
        for aluno in alunos:
            print(
                f"Matrícula: {aluno['matricula']}, Nome: {aluno['nome']}, Email: {aluno['email']}"
            )
    print("\n")


# Função para excluir um aluno com base na matrícula
def excluir_aluno():
    """
    Exclui um aluno com base na matrícula fornecida pelo usuário.
    """
    matricula = input("Digite a matrícula do aluno para excluir: ").strip()
    aluno = next((a for a in alunos if a["matricula"] == matricula), None)

    if aluno:
        alunos.remove(aluno)
        print(f"Aluno com matrícula {matricula} excluído com sucesso!\n")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.\n")
