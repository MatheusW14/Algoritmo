import random
import string 

alunos = []

def gerar_matricula():
    numero = random.randint(1, 9999)
    letra = random.choice(string.ascii_uppercase) # random.choice() escolhe um único elemento aleatório de uma sequência (lista, tupla, string, etc.).
    matricula = f"{numero:04}{letra}"
    return matricula


def cadastrar_aluno():
    matricula = gerar_matricula()
    
    campos = [
        "Digite o nome do aluno:",
        "Digite a data de nascimento (DD/MM/AAAA):",
        "Digite o sexo (M/F):",
        "Digite o endereço:",
        "Digite o telefone (apenas números):",
        "Digite o email:",
    ]
    
    respostas = [input(campo).strip() for campo in campos]
    
    aluno = {
        "nome": respostas[0],
        "matricula": matricula, 
        "data_nascimento": respostas[1],
        "sexo": respostas[2],
        "endereco": respostas[3],
        "telefone": respostas[4],
        "email": respostas[5]
    }
    
    alunos.append(aluno)
    print(f"Aluno {aluno['nome']} cadastrado com sucesso!\n")
     

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
    else:
        print("\n=== Lista de Alunos ===")
        for aluno in alunos:
            print(f"Matrícula: {aluno['matricula']}, Nome: {aluno['nome']}, Email: {aluno['email']}")
    print("\n")

# Função para excluir um aluno com base na matrícula
def excluir_aluno():
    matricula = input("Digite a matrícula do aluno para excluir: ").strip()
    aluno = next((a for a in alunos if a['matricula'] == matricula), None)
    
    if aluno:
        alunos.remove(aluno)
        print(f"Aluno com matrícula {matricula} excluído com sucesso!\n")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.\n")

