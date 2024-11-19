from random import randint

print("*** JOGO PARA ADIVINHAR O NUMÉRO ***")
print("************************************")

nome = input("Digite seu nome:")

print("Bem vindo {nome}, eu pensei em um número, tente adivinhar....")

num_tentativas = 5

print("num_tentativas ")
sorteio = randint(0, 5)

while num_tentativas > 0:

    chute = int(input("Em qual número pensei (0 - 5)?"))

    if chute == sorteio:
        print(f"Muito bem {nome}, você acertou")
        break
    else:
        print("Poxa, você infelizmente não acertou!")
        num_tentativas <= 1
print(f"Que pena {nome}, o numero que pensei foi {sorteio}")