import pickle
import os

# Função para carregar os dados
def carregar_dados():
    # Pega o diretório do script atual e cria o caminho para o arquivo
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'dados.pickle')
    try:
        with open(caminho_arquivo, 'rb') as f:
            alunos = pickle.load(f)
            professores = pickle.load(f)
            disciplinas = pickle.load(f)
            turmas = pickle.load(f)
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        alunos = []
        professores = []
        disciplinas = []
        turmas = []
        print("Nenhum dado encontrado. Iniciando com listas vazias.")
    return alunos, professores, disciplinas, turmas

# Função para salvar os dados
def salvar_dados(alunos, professores, disciplinas, turmas):
    # Pega o diretório do script atual e cria o caminho para o arquivo
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'dados.pickle')
    
     # Verifica se os dados estão sendo passados corretamente
    print("Salvando dados...")
    print("Alunos:", alunos)
    print("Professores:", professores)
    print("Disciplinas:", disciplinas)
    print("Turmas:", turmas)

    with open(caminho_arquivo, 'wb') as f:
        pickle.dump(alunos, f)
        pickle.dump(professores, f)
        pickle.dump(disciplinas, f)
        pickle.dump(turmas, f)
    print("Dados salvos com sucesso!")
