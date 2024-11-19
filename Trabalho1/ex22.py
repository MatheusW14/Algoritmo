def contar_vogais_consoantes(frase):
    vogais = "a, e, i, o, u, A, E, I, O, U"  
    num_vogais = 0
    num_consoantes = 0 
    for letra in frase:
        if ('a' <= letra <= 'z') or ('A' <= letra <= 'Z'):  
            if letra in vogais:  
                num_vogais += 1
            else:  
                num_consoantes += 1
    return num_vogais, num_consoantes


frase = input("Digite uma frase: ")


vogais, consoantes = contar_vogais_consoantes(frase)


print(f"Número de vogais na frase é: {vogais}")
print(f"Número de consoantes na frase é: {consoantes}")