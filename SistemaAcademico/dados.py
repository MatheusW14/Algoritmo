import pickle

# Função para carregar os dados
def carregar_dados():
    try:
        with open('dados.pickle', 'rb') as f:
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
    with open('dados.pickle', 'wb') as f:
        pickle.dump(alunos, f)
        pickle.dump(professores, f)
        pickle.dump(disciplinas, f)
        pickle.dump(turmas, f)
    print("Dados salvos com sucesso!")
