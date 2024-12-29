from rich.console import Console
from rich.table import Table
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
    console = Console()

    carregar_dados()

    while True:
        # Criando uma tabela bonita para o menu
        table = Table(title="Sistema de Gerenciamento Acadêmico")

        table.add_column("Opção", style="cyan", justify="center")
        table.add_column("Descrição", style="magenta")

        # Adicionando as opções do menu
        table.add_row("01", "Cadastrar Aluno")
        table.add_row("02", "Cadastrar Professor")
        table.add_row("03", "Cadastrar Disciplina")
        table.add_row("04", "Cadastrar Turma")
        table.add_row("05", "Inserir Professor em Disciplina")
        table.add_row("06", "Inserir Disciplinas em Turma")
        table.add_row("07", "Listar Professores")
        table.add_row("08", "Listar Alunos")
        table.add_row("09", "Listar Disciplinas")
        table.add_row("10", "Listar Turmas")
        table.add_row("11", "Matricular Aluno em Turma")
        table.add_row("12", "Filtrar Professores por Disciplina")
        table.add_row("13", "Consultar Alunos por Turma")
        table.add_row("14", "Consultar Professor por Disciplina")
        table.add_row("15", "Consultar Disciplinas por Turma")
        table.add_row("16", "Excluir Aluno")
        table.add_row("17", "Excluir Professor")
        table.add_row("18", "Excluir Disciplina")
        table.add_row("19", "Excluir Turmas")
        table.add_row("20", "Sair")

        console.print(table)  # Imprime a tabela de opções

        opcao = input("Escolha uma opção: ").strip()

        # Condições para chamar a função de acordo com a escolha do usuário
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
            console.print("Sistema encerrado.", style="bold red")
            break
        else:
            console.print("Opção inválida! Tente novamente.", style="bold red")


menu()
