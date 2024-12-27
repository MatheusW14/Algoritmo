from alunos import cadastrar_aluno, listar_alunos, excluir_aluno
from professores import cadastrar_professores, listar_professores, excluir_professor
from disciplinas import cadastrar_disciplina, listar_disciplinas, excluir_disciplina
from dados import carregar_dados, salvar_dados

alunos, professores, disciplinas, turmas = carregar_dados()

def menu():
    while True:
        print("01. Cadastrar Aluno")
        print("02. Cadastrar Professor")
        print("03. Cadastrar Disciplinas")
        print("04. Listar Professores")
        print("05. Listar Alunos")
        print("06. Listar Disciplinas")
        print("07. Excluir Aluno")
        print("08. Excluir Professor")
        print("09. Excluir Disciplina")
        print("10. Sair")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            cadastrar_professores()
        elif opcao == "3":
            cadastrar_disciplina()
        elif opcao == "4":
            listar_professores()
        elif opcao == "5":
            listar_alunos()
        elif opcao == "6":
            listar_disciplinas()
        elif opcao == "7":
            excluir_aluno()
        elif opcao == "8":
            excluir_professor()
        elif opcao == "9":
            excluir_disciplina()
        elif opcao == "10":
            salvar_dados(alunos, professores, disciplinas, turmas)
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida! Tente novamente.\n")
            
menu()