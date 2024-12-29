from alunos import cadastrar_aluno, listar_alunos, excluir_aluno
from professores import (
    cadastrar_professores,
    listar_professores,
    excluir_professor,
    filtrar_professores_por_disciplina,
)
from disciplinas import (
    cadastrar_disciplina,
    listar_disciplinas,
    excluir_disciplina,
    inserir_professor_em_disciplina,
    consultar_professor_por_disciplina,
)
from turmas import (
    cadastrar_turma,
    listar_turmas,
    excluir_turma,
    matricular_aluno_em_turma,
    inserir_disciplinas_em_turma,
    consultar_alunos_por_turma,
    consultar_disciplinas_por_turma,
)
from dados import carregar_dados, salvar_dados


def menu():

    carregar_dados()

    while True:
        print("01. Cadastrar Aluno")
        print("02. Cadastrar Professor")
        print("03. Cadastrar Disciplinas")
        print("04. Cadastrar Turmas")
        print("05. Inserir Professor em Disciplina")
        print("06. Inserir Disciplinas em Turma")
        print("07. Listar Professores")
        print("08. Listar Alunos")
        print("09. Listar Disciplinas")
        print("10. Listar Turmas")
        print("11. Matricular Aluno em Turma")
        print("12. Filtrar Professores por Disciplina")
        print("13. Consultar Alunos por Turma")
        print("14. Consultar Professor por Disciplina")
        print("15. Consultar Disciplinas por Turma")
        print("16. Excluir Aluno")
        print("17. Excluir Professor")
        print("18. Excluir Disciplina")
        print("19. Excluir Turmas")
        print("20. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "01":
            cadastrar_aluno()
        elif opcao == "02":
            cadastrar_professores()
        elif opcao == "03":
            cadastrar_disciplina()
        elif opcao == "04":
            cadastrar_turma()
        elif opcao == "05":
            inserir_professor_em_disciplina()
        elif opcao == "06":
            inserir_disciplinas_em_turma()
        elif opcao == "07":
            listar_professores()
        elif opcao == "08":
            listar_alunos()
        elif opcao == "09":
            listar_disciplinas()
        elif opcao == "10":
            listar_turmas()
        elif opcao == "11":
            matricular_aluno_em_turma()
        elif opcao == "12":
            filtrar_professores_por_disciplina()
        elif opcao == "13":
            consultar_alunos_por_turma()
        elif opcao == "14":
            consultar_professor_por_disciplina()
        elif opcao == "15":
            consultar_disciplinas_por_turma()
        elif opcao == "16":
            excluir_aluno()
        elif opcao == "17":
            excluir_professor()
        elif opcao == "18":
            excluir_disciplina()
        elif opcao == "19":
            excluir_turma()
        elif opcao == "20":
            salvar_dados()
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida! Tente novamente.\n")


menu()
