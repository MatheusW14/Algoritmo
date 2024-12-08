import random
import string 

professores = []

def gerar_matricula():
    numero = random.randint(10000, 99999)
    letra = random.choice(string.ascii_uppercase) # random.choice() escolhe um único elemento aleatório de uma sequência (lista, tupla, string, etc.).
    matricula = f"{numero:05}{letra}"
    return matricula

def cadastrar_professores():
    id_professor = gerar_matricula()
    
    campos = [
        "Digite o nome do professor:",
        "Digite a data de nascimento:",
        "Digite o sexo(M/F):",
        "Digite o endereço:",
        "Digite o telefone(apenas números):",
        "Digite o email:"
        "Digite as diciplinas leciondas (separadas por vírgulas):"
    ]
    
    respostas = [input(campo).strip() for campo in campos]
    
    disciplinas = [disciplina.strip() for disciplina in respostas[6].split(",")]  # As disciplinas serão separadas por vírgulas e convertidas em uma lista
    
    professor = {
        "nome": respostas[0],
        "id_professor": id_professor,
        "data_nascimento": respostas[1],
        "sexo": respostas[2],
        "endereco": respostas[3],
        "telefone": respostas[4],
        "email": respostas[5],
        "disciplinas": disciplinas,
    }
    professores.append(professor)
    print(f"Professor {professor['nome']} cadastrado com sucesso!\n")