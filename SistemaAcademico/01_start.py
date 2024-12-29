from alunos import cadastrar_aluno, listar_alunos, excluir_aluno
from professores import cadastrar_professores, listar_professores, excluir_professor
from disciplinas import cadastrar_disciplina, listar_disciplinas, excluir_disciplina, inserir_professor_em_disciplina
from turmas import cadastrar_turma, listar_turmas, excluir_turma, matricular_aluno_em_turma, inserir_disciplinas_em_turma
from dados import carregar_dados, salvar_dados

def menu():
    
    carregar_dados()
    
    while True:
        print("01. Cadastrar Aluno")
        print("02. Cadastrar Professor")
        print("03. Cadastrar Disciplinas")
        print("04. Cadastrar Turmas")
        print("04. Inserir Professor em Disciplina")
        print("04. Inserir Disciplinas em Turma")
        print("05. Listar Professores")
        print("06. Listar Alunos")
        print("07. Listar Disciplinas")
        print("08. Listar Turmas")
        print("08. Matricular Aluno em Turma")
        print("09. Excluir Aluno")
        print("10. Excluir Professor")
        print("11. Excluir Disciplina")
        print("12. Excluir Turmas")
        print("13. Sair")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            cadastrar_professores()
        elif opcao == "3":
            cadastrar_disciplina()
        elif opcao == "4":
            cadastrar_turma()
        elif opcao == "4":
            inserir_professor_em_disciplina()
        elif opcao == "4":
            inserir_disciplinas_em_turma()
        elif opcao == "5":
            listar_professores()
        elif opcao == "6":
            listar_alunos()
        elif opcao == "7":
            listar_disciplinas()
        elif opcao == "8":
            listar_turmas()
        elif opcao == "8":
            matricular_aluno_em_turma()
        elif opcao == "9":
            excluir_aluno()
        elif opcao == "10":
            excluir_professor()
        elif opcao == "11":
            excluir_disciplina()
        elif opcao == "12":
            excluir_turma()
        elif opcao == "13":
            salvar_dados()
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida! Tente novamente.\n")
            
menu()