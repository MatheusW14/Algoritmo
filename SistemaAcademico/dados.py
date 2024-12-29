import os
import pickle
from alunos import alunos
from professores import professores
from disciplinas import disciplinas
from turmas import turmas

# Caminho absoluto para o arquivo 'dados.pickle' no mesmo diretório do script
caminho_arquivo = os.path.join(os.path.dirname(__file__), 'dados.pickle')

# Função para carregar os dados
def carregar_dados():
    try:
        with open(caminho_arquivo, 'rb') as f:
            alunos[:] = pickle.load(f)  # Atualiza a lista de alunos
            professores[:] = pickle.load(f)
            disciplinas[:] = pickle.load(f)
            turmas[:] = pickle.load(f)  
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Nenhum dado encontrado. Iniciando com listas vazias.")

# Função para salvar os dados
def salvar_dados():
    with open(caminho_arquivo, 'wb') as f:
        # Salva as listas no arquivo pickle
        pickle.dump(alunos, f)
        pickle.dump(professores, f)
        pickle.dump(disciplinas, f)
        pickle.dump(turmas, f) 
    print("Dados salvos com sucesso!")
