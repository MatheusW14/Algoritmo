def tabuada(num):
    for i in range(1, 11):  # vai de 1 a 10
        print(f"{num} x {i} = {num * i}")

num = int(input("Digite um número para conhecer sua tabuada: "))

tabuada(num)
