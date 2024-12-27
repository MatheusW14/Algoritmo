import random
from professores import listar_professores # Importa a função listar_professores e a lista professores do módulo professores

disciplinas = []

def gerar_codigo():
    return f"D-{random.randint(1000, 9999)}"
def cadastrar_disciplina():
    codigo = gerar_codigo()
    print(f"Código da disciplina gerado: {codigo}")
    
    nome = input("Digite o nome da disciplina: ").strip()
    carga_horaria = input("Digite a carga horária (em horas): ").strip()
    
    # Exibe a lista de professores cadastrados usando a função listar_professores()
    listar_professores()
    
    # Solicita ao usuário que escolha um professor
    professor_escolhido = input("Escolha o ID do professor que irá ministrar a disciplina: ").strip()

    from professores import professores  # Importa a lista de professores

    professor = next((prof for prof in professores if prof['id_professor'] == professor_escolhido), None)
    
    if not professor:
        print("Professor não encontrado. Cadastro cancelado.\n")
        return
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
    
def excluir_disciplina():
    codigo = input("Digite o código da disciplina para excluir: ").strip()
    disciplina = next((d for d in disciplinas if d['codigo'] == codigo), None)
    
    if disciplina:
        disciplinas.remove(disciplina)
        print(f"Disciplina com código {codigo} excluída com sucesso!\n")
    else:
        print(f"Disciplina com código {codigo} não encontrada.\n")

