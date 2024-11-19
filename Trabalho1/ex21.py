def remover_duplicados(lista):
    lista_sem_duplicados = []  
    for num in lista:  
        if num not in lista_sem_duplicados: 
            lista_sem_duplicados.append(num)  
    return lista_sem_duplicados 


entrada = input("Digite uma lista de números inteiros, separados por espaço: ")

lista = [int(x) for x in entrada.split()]

resultado = remover_duplicados(lista)

print(f"A lista sem duplicados é: {resultado}")
