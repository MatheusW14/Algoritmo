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
            dados = pickle.load(f)
            if not isinstance(dados, list) or len(dados) != 4:
                raise ValueError("Arquivo de dados corrompido ou formato inválido.")
            alunos[:], professores[:], disciplinas[:], turmas[:] = dados
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Nenhum dado encontrado. Iniciando com listas vazias.")
    except (ValueError, EOFError) as e:
        print(f"Erro ao carregar os dados: {e}. Iniciando com listas vazias.")


# Função para salvar os dados
def salvar_dados():
    try:
        with open(caminho_arquivo, 'wb') as f:
            pickle.dump([alunos, professores, disciplinas, turmas], f)
        print("Dados salvos com sucesso!")
    except (IOError, pickle.PickleError) as e:
        print(f"Erro ao salvar os dados: {e}")

