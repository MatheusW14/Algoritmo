import random
num = int(input("Digite um num de 1-10:"))

sorteio = random.randint(1, 10)

if num == sorteio :
    print("Voce acertou!")
else:
    sorteio = random.randint(1, 5)
    print("Vc errou!, tente novamente")