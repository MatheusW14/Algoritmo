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

def excluir_turma():
    if not turmas:
        print("Nenhuma turma cadastrada ainda.")
        return
    print("\n=== Turmas Disponíveis ===")
    for i, turma in enumerate(turmas, start=1):
        print(f"{i}. {turma['nome']} (Código: {turma['codigo']})")
    try:
        escolha = int(input("Digite o número da turma a excluir: ").strip())
        if escolha < 1 or escolha > len(turmas):
            raise ValueError
    except ValueError:
        print("Opção inválida. Exclusão cancelada.")
        return
    turma_excluida = turmas.pop(escolha - 1)
    print(f"Turma '{turma_excluida['nome']}' excluída com sucesso!")
    
def matricular_aluno_em_turma():
    if not turmas:
        print("Nenhuma turma cadastrada. Cadastro cancelado.")
        return

    # Listar turmas
    print("\nEscolha uma turma para matricular o aluno:")
    for i, turma in enumerate(turmas, start=1):
        print(f"{i}. {turma['nome']} (Código: {turma['codigo']})")

    escolha_turma = int(input("Digite o número correspondente da turma: ").strip())
    if escolha_turma < 1 or escolha_turma > len(turmas):
        print("Opção inválida. Matrícula cancelada.")
        return

    turma_selecionada = turmas[escolha_turma - 1]

    if not alunos:
        print("Nenhum aluno cadastrado. Matrícula cancelada.")
        return

    # Listar alunos
    print("\nEscolha um aluno para matricular:")
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. {aluno['nome']} (Matrícula: {aluno['matricula']})")

    escolha_aluno = int(input("Digite o número correspondente do aluno: ").strip())
    if escolha_aluno < 1 or escolha_aluno > len(alunos):
        print("Opção inválida. Matrícula cancelada.")
        return

    aluno_selecionado = alunos[escolha_aluno - 1]

    # Verificar se o aluno já está matriculado na turma
    if aluno_selecionado in turma_selecionada['alunos']:
        print(f"O aluno {aluno_selecionado['nome']} já está matriculado nesta turma.")
        return

    # Adicionar aluno à turma
    turma_selecionada['alunos'].append(aluno_selecionado)
    print(f"Aluno {aluno_selecionado['nome']} matriculado com sucesso na turma {turma_selecionada['nome']}!")