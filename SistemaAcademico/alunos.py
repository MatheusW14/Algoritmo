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
    print(f"Número de matrícula gerado: {matricula}")
    
    campos = [
        "Digite o nome do aluno:",
        "Digite a data de nascimento (DD/MM/AAAA):",
        "Digite o sexo (M/F)",
        "Digite o endereço:",
        "Digite o telefone (apenas números):",
        "Digite o email:",
    ]
    
    respostas = [input (campo).strip() for compo in campos]
    
    aluno = {
        "nome": respostas[0],
        "matricula": matricula, 
        "data_nascimente": respostas[1],
        "sexo": respostas[2],
        "endereço": respostas[3],
        "telefone": respostas[4],
        "email": respostas[5]
    }
    
    alunos.append(aluno)
    print(f"Aluno {aluno['nome']} cadastrado com sucersso!\n")