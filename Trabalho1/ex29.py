def remover_duplicados(lista_aninhada):
    nova_lista = []  
    for sublista in lista_aninhada:
        nova_lista.append(list(set(sublista))) 
    return nova_lista


entrada = input("Digite as sublistas, separadas por ponto e vírgula (exemplo: 1, 2, 3; 4, 5, 6): ")

lista_aninhada = []
for sublista in entrada.split(';'):
    lista_aninhada.append([int(x) for x in sublista.split(',')])


resultado = remover_duplicados(lista_aninhada)


print(f"A nova lista sem duplicados é: {resultado}")
