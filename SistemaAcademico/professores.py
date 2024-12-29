import random
import string 
from utils import obter_entrada

professores = []

def gerar_matricula():
    numero = random.randint(10000, 99999)
    letra = random.choice(string.ascii_uppercase) 
    matricula = f"{numero:05}{letra}"
    return matricula

def cadastrar_professores():
    id_professor = gerar_matricula()
    
    nome = obter_entrada("Digite o nome do professor: ")
    data_nascimento = obter_entrada("Digite a data de nascimento (DD/MM/AAAA): ", validacao=lambda x: len(x) == 10 and x[2] == '/' and x[5] == '/')
    sexo = obter_entrada("Digite o sexo (M/F): ", validacao=lambda x: x in ['M', 'F'], erro="Sexo deve ser 'M' ou 'F'. Tente novamente.")
    endereco = obter_entrada("Digite o endereço: ")
    telefone = obter_entrada("Digite o telefone (apenas números): ", validacao=lambda x: x.isdigit(), erro="Telefone deve conter apenas números. Tente novamente.")
    email = obter_entrada("Digite o email: ")
    
    disciplinas = obter_entrada("Digite as disciplinas lecionadas (separadas por vírgulas): ").split(",")
    
    professor = {
        "nome": nome,
        "id_professor": id_professor,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "disciplinas": [disciplina.strip() for disciplina in disciplinas],  # Limpa espaços extras
    }
    
    professores.append(professor)
    print(f"Professor {professor['nome']} cadastrado com sucesso!\n")


    
def listar_professores():
    if not professores:
        print("Nenhum professor cadastrado ainda.")
    else:
        print("\n=== Lista de Professores ===")
        for professor in professores:
            print(f"ID: {professor['id_professor']}, Nome: {professor['nome']}, Disciplinas: {', '.join(professor['disciplinas'])}")
    print("\n")
    
def excluir_professor():
    professor_id = input("Digite o ID do professor para excluir: ").strip()
    professor = next((p for p in professores if p['id_professor'] == professor_id), None)
    
    if professor:
        professores.remove(professor)
        print(f"Professor com ID {professor_id} excluído com sucesso!\n")
    else:
        print(f"Professor com ID {professor_id} não encontrado.\n")

