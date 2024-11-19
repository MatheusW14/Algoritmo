# Criar um laço para imprimir somente os numeros divisiveis por 4, de 1 até um número gerado de firma aleatória (10 - 50)

from random import randint

num = randint(10, 50)
i = 0

while i <= num: 
    if i % 4 == 0:
        print(i)
    i += 1