import random
from SistemaAcademico import professores  # Importa a lista de professores cadastrados

disciplinas = []

def gerar_codigo():
    return f"D-{random.randint(1000, 9999)}"


def cadastrar_disciplina():
    codigo = gerar_codigo()
    print(f"Código da disciplina gerado: {codigo}")
    
    nome = input("Digite o nome da disciplina: ").strip()
    carga_horaria = input("Digite a carga horária (em horas): ").strip()
    
    print("=== Professores Cadastrados ===")
    for i, professor in enumerate(professores, start=1):
        print(f"{i}. ID: {professor['id_professor']}, Nome: {professor['nome']}")
    
    professor_escolhido = input("Escolha o número correspondente ao professor: ").strip()
    if not professor_escolhido.isdigit() or not (1 <= int(professor_escolhido) <= len(professores)):
        print("Opção inválida. Cadastro cancelado.\n")
        return
    
    professor = professores[int(professor_escolhido) - 1]
    
    disciplina = {
        "codigo": codigo,
        "nome": nome,
        "carga_horaria": carga_horaria,
        "professor": {
            "id": professor["id_professor"],
            "nome": professor["nome"],
        },
    }
    
    disciplinas.append(disciplina)
    print(f"Disciplina '{disciplina['nome']}' cadastrada com sucesso!\n")

def listar_disciplinas():
    if not disciplinas:
        print("Nenhuma disciplina cadastrada ainda.")
    else:
        print("\n=== Lista de Disciplinas ===")
        for disciplina in disciplinas:
            print(
                f"Código: {disciplina['codigo']}, Nome: {disciplina['nome']}, "
                f"Carga Horária: {disciplina['carga_horaria']}h, "
                f"Professor: {disciplina['professor']['nome']} (ID: {disciplina['professor']['id']})"
            )
    print("\n")