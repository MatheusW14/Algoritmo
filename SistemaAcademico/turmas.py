import random
from disciplinas import disciplinas
from professores import professores
from alunos import alunos

turmas = []


def gerar_codigo_turma():
    return f"T-{random.randint(1000, 9999)}"


def cadastrar_turma():
    nome = input("Digite o nome da turma: ").strip()
    codigo = gerar_codigo_turma()

    # Seleciona disciplina por índice
    if not disciplinas:
        print("Nenhuma disciplina cadastrada. Cadastro cancelado.")
        return
    print("Escolha uma disciplina para a turma:")
    for i, disciplina in enumerate(disciplinas, start=1):
        print(f"{i}. {disciplina['nome']} (Código: {disciplina['codigo']})")
    escolha_disciplina = int(input("Digite o número correspondente: ").strip())
    if escolha_disciplina < 1 or escolha_disciplina > len(disciplinas):
        print("Opção inválida. Cadastro cancelado.")
        return
    disciplina_selecionada = disciplinas[escolha_disciplina - 1]

    # Seleciona professor por índice
    if not professores:
        print("Nenhum professor cadastrado. Cadastro cancelado.")
        return
    print("Escolha um professor para a turma:")
    for i, professor in enumerate(professores, start=1):
        print(f"{i}. {professor['nome']} (ID: {professor['id_professor']})")
    escolha_professor = int(input("Digite o número correspondente: ").strip())
    if escolha_professor < 1 or escolha_professor > len(professores):
        print("Opção inválida. Cadastro cancelado.")
        return
    professor_selecionado = professores[escolha_professor - 1]

    # Solicita lista de matrículas dos alunos
    if not alunos:
        print("Nenhum aluno cadastrado. Cadastro cancelado.")
        return
    print("Digite as matrículas dos alunos (separadas por vírgula):")
    print("Alunos disponíveis:")
    for aluno in alunos:
        print(f"{aluno['nome']} (Matrícula: {aluno['matricula']})")
    matriculas = input("Matrículas: ").strip().split(",")

    # Filtra apenas as matrículas válidas
    alunos_selecionados = [
        aluno for aluno in alunos if aluno['matricula'] in matriculas
    ]
    if not alunos_selecionados:
        print("Nenhuma matrícula válida foi inserida. Cadastro cancelado.")
        return

    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplina": disciplina_selecionada,
        "professor": professor_selecionado,
        "alunos": alunos_selecionados,
    }
    turmas.append(turma)
    print(f"Turma '{nome}' cadastrada com sucesso!")

def listar_turmas():
    if not turmas:
        print("Nenhuma turma cadastrada ainda.")
        return
    print("\n=== Lista de Turmas ===")
    for turma in turmas:
        print(
            f"Nome: {turma['nome']}, Código: {turma['codigo']}, "
            f"Disciplina: {turma['disciplina']['nome']}, "
            f"Professor: {turma['professor']['nome']}, "
            f"Alunos: {', '.join([aluno['nome'] for aluno in turma['alunos']])}"
        )
    print("\n")
