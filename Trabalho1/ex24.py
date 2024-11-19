def verificar_anagrama(palavra1, palavra2):
    if sorted(palavra1) == sorted(palavra2): #sorted ordena as letras da palavra em ordem alfabética.
        return True  
    else:
        return False 


palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")


resultado = verificar_anagrama(palavra1, palavra2)


if resultado:
    print(f"As palavras '{palavra1}' e '{palavra2}' são anagramas!")
else:
    print(f"As palavras '{palavra1}' e '{palavra2}' não são anagramas.")
