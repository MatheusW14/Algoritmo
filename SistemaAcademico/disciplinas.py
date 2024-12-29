import random
from professores import listar_professores, professores
from utils import obter_entrada

disciplinas = []

def gerar_codigo():
    return f"D-{random.randint(1000, 9999)}"

def cadastrar_disciplina():
    codigo = gerar_codigo()
    print(f"Código da disciplina gerado: {codigo}")
    
    nome = input("Digite o nome da disciplina: ").strip()
    carga_horaria = input("Digite a carga horária (em horas): ").strip()

    listar_professores()
    
    professor_escolhido = input("Escolha o ID do professor que irá ministrar a disciplina: ").strip()

    from professores import professores  

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
    codigo = obter_entrada("Digite o código da disciplina para excluir: ")
    disciplina = next((d for d in disciplinas if d['codigo'] == codigo), None)
    
    if disciplina:
        confirmacao = input(f"Tem certeza que deseja excluir a disciplina {disciplina['nome']}? (S/N): ").strip().upper()
        if confirmacao == "S":
            disciplinas.remove(disciplina)
            print(f"Disciplina com código {codigo} excluída com sucesso!\n")
        else:
            print("Operação cancelada.\n")
    else:
        print(f"Disciplina com código {codigo} não encontrada.\n")
        
def inserir_professor_em_disciplina():
  
    if not professores:
        print("Nenhum professor cadastrado. Cadastro cancelado.")
        return
    
    if not disciplinas:
        print("Nenhuma disciplina cadastrada. Cadastro cancelado.")
        return
    
    listar_disciplinas()
    
    codigo_disciplina = input("Digite o código da disciplina para alocar o professor: ").strip()
    disciplina = next((d for d in disciplinas if d['codigo'] == codigo_disciplina), None)
    
    if not disciplina:
        print("Disciplina não encontrada. Cadastro cancelado.")
        return

    listar_professores()

    professor_id = input("Digite o ID do professor para alocar: ").strip()
    professor = next((p for p in professores if p['id_professor'] == professor_id), None)

    if not professor:
        print("Professor não encontrado. Cadastro cancelado.")
        return

    disciplina['professor'] = {
        "id": professor["id_professor"],
        "nome": professor["nome"]
    }

    print(f"Professor {professor['nome']} alocado à disciplina '{disciplina['nome']}' com sucesso!")

