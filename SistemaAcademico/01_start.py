from alunos import cadastrar_aluno, listar_alunos
from professores import cadastrar_professores, listar_professores

while True:
    print("1. Cadastrar Aluno")
    print("2. Cadastrar Professor")
    print("3. Listar Professores")
    print("4. Listar Alunos")
    print("5. Sair")
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        cadastrar_professores()
    elif opcao == "3":
        listar_professores()
    elif opcao == "4":
        listar_alunos()
    elif opcao == "5":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.\n")