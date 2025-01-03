import random
import string
from utils import obter_entrada

professores = []


def gerar_matricula():
    """
    Gera uma matrícula única para um professor.

    Returns:
        str: A matrícula gerada no formato 'NNNNNL', onde 'N' é um dígito e 'L' é uma letra maiúscula.
    """
    numero = random.randint(10000, 99999)
    letra = random.choice(string.ascii_uppercase)
    matricula = f"{numero:05}{letra}"
    return matricula


def cadastrar_professores():
    """
    Cadastra um novo professor no sistema, solicitando as informações necessárias ao usuário.
    """
    id_professor = gerar_matricula()

    nome = obter_entrada("Digite o nome do professor: ")
    data_nascimento = obter_entrada(
        "Digite a data de nascimento (DD/MM/AAAA): ",
        validacao=lambda x: len(x) == 10 and x[2] == "/" and x[5] == "/",
    )
    sexo = obter_entrada(
        "Digite o sexo (M/F): ",
        validacao=lambda x: x in ["M", "F"],
        erro="Sexo deve ser 'M' ou 'F'. Tente novamente.",
    )
    endereco = obter_entrada("Digite o endereço: ")
    telefone = obter_entrada(
        "Digite o telefone (apenas números): ",
        validacao=lambda x: x.isdigit(),
        erro="Telefone deve conter apenas números. Tente novamente.",
    )
    email = obter_entrada("Digite o email: ")

    disciplinas = obter_entrada(
        "Digite as disciplinas lecionadas (separadas por vírgulas): "
    ).split(",")

    professor = {
        "nome": nome,
        "id_professor": id_professor,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "disciplinas": [
            disciplina.strip() for disciplina in disciplinas
        ],  # Limpa espaços extras
    }

    professores.append(professor)
    print(f"Professor {professor['nome']} cadastrado com sucesso!\n")


def listar_professores():
    """
    Lista todos os professores cadastrados no sistema.
    """
    if not professores:
        print("Nenhum professor cadastrado ainda.")
    else:
        print("\n=== Lista de Professores ===")
        for professor in professores:
            print(
                f"ID: {professor['id_professor']}, Nome: {professor['nome']}, Disciplinas: {', '.join(professor['disciplinas'])}"
            )
    print("\n")


def excluir_professor():
    """
    Exclui um professor com base no ID fornecido pelo usuário.
    """
    if not professores:
        print("Nenhum professor cadastrado para exclusão.\n")
        return

    # Listar todos os professores
    print("\n=== Lista de Professores Cadastrados ===")
    for professor in professores:
        print(f"ID: {professor['id']}, Nome: {professor['nome']}")
    print()

    id_professor = input("Digite o ID do professor para excluir: ").strip()
    professor = next((p for p in professores if p["id"] == id_professor), None)

    if professor:
        professores.remove(professor)
        print(f"Professor com ID {id_professor} excluído com sucesso!\n")
    else:
        print(f"Professor com ID {id_professor} não encontrado.\n")


def filtrar_professores_por_disciplina():
    """
    Filtra e exibe os professores que ministram uma disciplina específica.
    """
    if not professores:
        print("Nenhum professor cadastrado no sistema.")
        return

    # Exibir lista de disciplinas disponíveis nos professores
    disciplinas_cadastradas = set(
        disciplina
        for professor in professores
        for disciplina in professor.get("disciplinas", [])
    )

    if not disciplinas_cadastradas:
        print("Nenhuma disciplina encontrada nos professores cadastrados.")
        return

    print("\n=== Disciplinas Disponíveis ===")
    for disciplina in sorted(disciplinas_cadastradas):
        print(f"- {disciplina}")

    # Solicitar ao usuário a disciplina para filtrar
    disciplina_escolhida = input("\nDigite o nome da disciplina para filtrar: ").strip()

    # Encontrar professores que ministram a disciplina escolhida
    professores_filtrados = [
        professor
        for professor in professores
        if disciplina_escolhida in professor.get("disciplinas", [])
    ]

    if not professores_filtrados:
        print(
            f"Nenhum professor encontrado para a disciplina '{disciplina_escolhida}'."
        )
    else:
        print(f"\n=== Professores que ministram '{disciplina_escolhida}' ===")
        for professor in professores_filtrados:
            print(f"ID: {professor['id_professor']}, Nome: {professor['nome']}")
