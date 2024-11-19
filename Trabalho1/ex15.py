import random

def jogo_adivinhar():
    numero_secreto = random.randint(1, 100) 
    tentativas = 0  

    print("Tente adivinhar o número que estou pensando, entre 1 e 100!")

    while True:
        chute = int(input("Digite seu palpite: ")) 
        tentativas += 1  

        if chute < numero_secreto:
            print("O número secreto é maior!")
        elif chute > numero_secreto:
            print("O número secreto é menor!")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break 

jogo_adivinhar()